import discord
import requests
from discord.ext import commands


class PypiCommmand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="pypi")
    async def pypi(self, bot, ctx, *, args):
        try:
            req = requests.get("https://pypi.org/pypi/{args}/json")
            if req.status_code == 200:
                resp = req.json()
                info = resp["info"]
                embed = discord.Embed(
                    title=f"La información sobre el paquete {args} es:",
                    description=f"""
                    Nombre: {info["name"]}
                    Resumen: {info["summary"]}
                    Autor: {info["author"]}
                    Licencia: {info["license"]}
                    Versión: {info["version"]}
                    Link del proyecto: {info["project_url"]}
                    HomePage: {info["home_page"]}
                    Versión de python: {info["requires_python"]}
                    """,
                    color=discord.Color.random(),
                )
                embed.set_thumbnail(
                    url="https://media1.tenor.com/images/ac9cf136a3c0f857e436c32561e9b6e8/tenor.gif"
                )
                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(
                    title="Error :x:",
                    description="Error en encontrar el paquete o la API",
                    footer=f"API STATUS: {req.status_code}",
                    color=discord.Color.random(),
                )
                embed.set_thumbnail(
                    url="https://media1.tenor.com/images/46ce1235c5697ce170c6e84f4b4fb4e7/tenor.gif"
                )
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


def setup(bot):
    bot.add_cog(PypiCommmand(bot))
