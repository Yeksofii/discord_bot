import discord
from discord.ext import commands
import config

class LoggingSystem(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # When someone joins
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.get_channel(config.LOG_CHANNEL_ID)
        if channel:
            await channel.send(f"🟢 **{member} joined the server.**")

    # When someone leaves
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = member.guild.get_channel(config.LOG_CHANNEL_ID)
        if channel:
            await channel.send(f"🔴 **{member} left the server.**")

    # Message deleted
    @commands.Cog.listener()
    async def on_message_delete(self, message):
        if message.author.bot:
            return
        channel = message.guild.get_channel(config.LOG_CHANNEL_ID)
        if channel:
            await channel.send(
                f"🗑️ **Message deleted in {message.channel.mention}**\n"
                f"**Author:** {message.author}\n"
                f"**Content:** {message.content}"
            )

    # Message edited
    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        if before.author.bot or before.content == after.content:
            return

        channel = before.guild.get_channel(config.LOG_CHANNEL_ID)
        if channel:
            await channel.send(
                f"✏️ **Message edited in {before.channel.mention}**\n"
                f"**Author:** {before.author}\n"
                f"**Before:** {before.content}\n"
                f"**After:** {after.content}"
            )

    # Ban logging
    @commands.Cog.listener()
    async def on_member_ban(self, guild, user):
        channel = guild.get_channel(config.LOG_CHANNEL_ID)
        if channel:
            await channel.send(f"⛔ **{user} was banned from the server.**")

async def setup(bot):
    await bot.add_cog(LoggingSystem(bot))
