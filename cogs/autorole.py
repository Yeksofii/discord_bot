import discord
from discord.ext import commands
import config

class AutoRole(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        role = member.guild.get_role(config.AUTO_ROLE_ID)
        if role:
            try:
                await member.add_roles(role)
                print(f"Gave autorole {role.name} to {member}")
            except discord.Forbidden:
                print("Missing permissions: cannot assign autorole.")

async def setup(bot):
    await bot.add_cog(AutoRole(bot))
