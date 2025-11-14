import discordfrom discord.ext import commands
import config

class Welcome(commands.Cog):
    def__init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        channel = member.guild.get_channel(config.WELCOME_CHANNEL_ID)
        if channel:
            await channel.send(f"Welcome to the server, {member.mention}!")

async def setup (bot):
    await bot.add_cog(Welcome(bot))
    