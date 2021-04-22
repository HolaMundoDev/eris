from discord.ext import commands
import discord
import requests


class CratesCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="crate")
    async def crate(self, ctx, *, args):
        req = requests.get(f"https://crates.io/api/v1/crates/{args}")
        try:
            if req.status_code == 200:
                resp = req.json()
                crateMain = resp["crate"]
                embed = discord.Embed(
                    title=f"La información del paquete {args} es:",
                    description=f"""
                    Nombre: {crateMain["name"]}
                    Descargas: {crateMain["downloads"]}
                    Descripción: {crateMain["description"]}
                    Palabras Clave: {crateMain["keywords"]}
                    Versión Máxima: {crateMain["max_version"]}
                    Versión Máxima Estable: {crateMain["max_stable_version"]}
                    Repositorio: {crateMain["repository"]}
                    Documentación: {crateMain["documentation"]}
                    Actualizado: {crateMain["updated_at"]}
                    """,
                    color=discord.Color.random(),
                    footer=f"API Estatus: {req.status_code}",
                )
                embed.set_thumbnail(
                    url="https://rustacean.net/more-crabby-things/animated-ferris.gif"
                )
                await ctx.send(embed=embed)
            elif req.status_code == 404:
                embed = discord.Embed(
                    title="Error :x:",
                    description="Crate Not Found",
                    color=discord.Color.red(),
                    footer=f"API Estatus: {req.status_code}",
                )
                embed.set_thumbnail(
                    url="https://media1.tenor.com/images/963dbf83410067b8216bf3fbeec50874/tenor.gif"
                )
                await ctx.send(embed=embed)

        except Exception as err:
            embed = discord.Embed(
                title="Error :x:",
                description=f"El error es: **{err}**",
                color=discord.Color.red(),
                footer=f"API Estatus: **{req.status_code}**",
            )
            embed.set_thumbnail(
                url="https://media1.tenor.com/images/963dbf83410067b8216bf3fbeec50874/tenor.gif"
            )
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(CratesCommand(bot))
