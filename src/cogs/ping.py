import time

from discord.ext import commands


class Ping_Command(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="ping", usage="", description="El bot responde pong")
    async def ping(self, ctx):
        before = time.monotonic()
        message = await ctx.send("🏓 Pong !")
        ping = (time.monotonic() - before) * 1000
        await message.edit(content=f"🏓 Pong !  `{int(ping)} ms`")


def setup(bot):
    bot.add_cog(Ping_Command(bot))