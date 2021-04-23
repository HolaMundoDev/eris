import discord
from discord.ext import commands


class help_command(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="help")
    async def help_command(self, ctx):
        comandos = """
        Los comandos de este maravilloso bot:
                
        **ping:** Muestra el ping del bot
        **avatar:** Muestra el avatar de otra persona
        **help:** Muestra este mensaje
        **ban:** Banea al usuario si tiene los permisos
        **kick:** Kickea al usuario si tiene los permisos
        **cita:** Muestra una cita inspiradora de varios filósofos
        **joke:** Muestra chistes que te divertirán
        **wiki:** Busca un termino en la wikipedia
        **npm:** Busca algún paquete en la API de NPM
        **crate:** Busca algún crate en la API de CRATES.IO
        **pypi:** Busca alguna librería en la API de PYPI
        **english:** Muestra la definción de una palabra en  inglés su significado y muchas cosas más
        
        Chao Mundo
        """
        embed = discord.Embed(
            title="Comando de Ayuda de este bot",
            description=comandos,
            color=discord.Color.random(),
        )
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(help_command(bot))
