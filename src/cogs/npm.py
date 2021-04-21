import discord
from discord.ext import commands
import requests
from requests.utils import requote_uri


class NpmCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="npm")
    async def npmSearch(self, ctx, *, args):
        parsed = requote_uri(args)

        req = requests.get(f"https://api.npms.io/v2/search?q={parsed}")

        if req.status_code != 200:
            embed = discord.Embed(
                title="Error API STATUS",
                description=f"Código de la API: {req.status_code}",
                color=discord.Color.red(),
            )
            embed.set_thumbnail(
                url="https://media1.tenor.com/images/46ce1235c5697ce170c6e84f4b4fb4e7/tenor.gif"
            )
            await ctx.send(embed=embed)
        elif req.status_code == 200:
            try:
                resp = req.json()
                results_info = resp["results"]
                resultsGet_info = results_info[0]
                pkgInfo = resultsGet_info["package"]
                linksPkg = pkgInfo["links"]
                embed = discord.Embed(
                    title=f"La información sobre el paquete **{args}** es: ",
                    description=f"""
                    Nombre: {pkgInfo["name"]}
                    Versión: {pkgInfo["version"]}
                    Descripción: {pkgInfo["description"]}
                    Fecha: {pkgInfo["date"]}
                    Link: {linksPkg["npm"]}
                  """,
                    color=discord.Color.random(),
                )
                embed.set_thumbnail(
                    url="https://authy.com/wp-content/uploads/npm-logo.png"
                )
                await ctx.send(embed=embed)

            except Exception as err:
                embed = discord.Embed(
                    title="Error API STATUS",
                    description=f"Código de la API: {err}",
                    color=discord.Color.red(),
                )
                embed.set_thumbnail(
                    url="https://media1.tenor.com/images/46ce1235c5697ce170c6e84f4b4fb4e7/tenor.gif"
                )
                await ctx.send(embed=embed)
        else:
            print(req.status_code)


def setup(bot):
    bot.add_cog(NpmCommand(bot))
