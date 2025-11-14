import discord
from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=none):
        await member.kick(reason=reason)
        await ctx.send(f"{member} has been kicked.")
    
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int):
        deleted = await ctx.channel.purge(limit amount)
        await ctx.send(f"🧹 Deleted {len(deleted)} messages.", delete_after=3)

async def setup(bot):
    await bot.add_cog(Moderation(bot)) 