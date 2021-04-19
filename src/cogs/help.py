import discord
from discord.ext import commands


class help_command(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="help")
    async def help_command(self, ctx):
        comandos = """
        Los comandos de este maravilloso bot:
                
        Ping: Muestra el ping del bot
        Avatar: Muestra el avatar de otra persona
        Help: Muestra este mensaje
        Ban: Banea al usuario si tiene los permisos
        Kick: Kickea al usuario si tiene los permisos
        Cita: Muestra una cita inspiradora de varios filósofos
        Joke: Muestra chistes que te divertirán
        Wiki: Busca un termino en la wikipedia
        
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
