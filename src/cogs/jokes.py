from discord.ext import commands
import requests


def fetch():
    url = "https://icanhazdadjoke.com/"
    headers = {"Accept": "application/json"}
    r = requests.get(url, headers=headers)
    return r


class Joke_Command(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name="joke",
        usage="",
        description="Consulta en la  api de icanhazdadjoke y trae un chiste",
    )
    async def joke(self, ctx):
        jokeMSG = fetch()
        if jokeMSG.status_code == 200:
            r = jokeMSG.json()
            await ctx.send(r["joke"])
        else:
            await ctx.send(":x: Ups... hubo un error en el servidor")


def setup(bot):
    bot.add_cog(Joke_Command(bot))
