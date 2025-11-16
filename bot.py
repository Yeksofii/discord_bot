import discord
from discord.ext import commands
import config
import asyncio

intents = discord.Intents.default()
intents.message_content = True  # Required for reading messages
intents.members = True          # Required for join/leave events
intents.guilds = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    print("Cogs loaded.")

# Load cogs in async main
async def main():
    async with bot:
        await bot.load_extension("cogs.welcome")
        await bot.load_extension("cogs.moderation")
        await bot.load_extension("cogs.music")
        await bot.load_extension("cogs.logging_system")
        await bot.load_extension("cogs.autorole")
        await bot.load_extension("cogs.ticket")
        await bot.start(config.TOKEN)

# Run bot
asyncio.run(main())

