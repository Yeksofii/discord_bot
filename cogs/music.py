import discord
from discord.ext import commands
import yt_dlp

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def search_youtube(self, query):
        ytdl_opts = {
            "format": "bestaudio/best",
            "quiet": True,
        }

        with yt_dlp.YoutubeDL(ytdl_opts) as ytdl:
            info = ytdl.extract_info(f"ytsearch:{query}", download=False)['entries'][0]
        return info['url']

    @commands.command()
    async def play(self, ctx, *, query):
        if not ctx.author.voice:
            return await ctx.send("You must be in a voice channel.")

        voice_channel = ctx.author.voice.channel

        if not ctx.voice_client:
            await voice_channel.connect()

        url = self.search_youtube(query)

        ctx.voice_client.stop()

        ffmpeg_opts = {
            "before_options": "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5",
            "options": "-vn",
        }

        source = await discord.FFmpegOpusAudio.from_probe(url, **ffmpeg_opts)
        ctx.voice_client.play(source)

        await ctx.send(f"🎶 Now playing: **{query}**")

    @commands.command()
    async def stop(self, ctx):
        if ctx.voice_client:
            ctx.voice_client.stop()
            await ctx.voice_client.disconnect()
            await ctx.send("⏹️ Music stopped.")

async def setup(bot):
    await bot.add_cog(Music(bot))
