import discord
from discord.ext import commands

class InfoCommand(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command(name="info")
    async def info(self,ctx):
        embed = discord.Embed(
            title = "La información de este maravilloso bot",
            description = """
            **Github:*** https://github.com/HolaMundoDev/discord-bot
            
            Para poder contribuir a este bot lo necesario es saber sobre python
            Leer la documentación de discord.py links abajo y ganas de colaborar
            Puedes preguntar a los mods o a los colaboradores sobre más detalles
            ahora puedes leer las normas de contribución en el github y colaborar
            si tu pull request es aprovado **Genial** si no se te dirá el por que y
            así pueda ser aprovado :+1: ahora que estás listo que esperas para contribuir.

            **Discord.py:** https://discordpy.readthedocs.io/en/stable/

            Chao Mundo
            """,
            color = discord.Color.random(),
            timestamp=ctx.message.created_at,
        )
        embed.set_thumbnail(url="https://media1.tenor.com/images/9e2cc1f421ac8fe67f5d4c7c7febb295/tenor.gif")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(InfoCommand(bot))
