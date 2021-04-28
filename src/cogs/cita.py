import discord
import requests
from discord.ext import commands


class InspireCog(commands.Cog, name="quote_command"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name="cita",
        usage="Usalo cuando no estes inspirado y quieras ayuda",
        description="Muestra frases de varios filósofos que te ayudan a inspirarte",
    )
    async def inspire(self, ctx):
        response = requests.get("https://zenquotes.io/api/random")
        status = response.status_code
        if status == int(200):
            global author
            global quote
            answer = response.json()
            data = answer[0]
            quote = data["q"]
            author = data["a"]
        embed = discord.Embed(
            title="Cita Inspiradora", description=quote, color=discord.Color.random()
        )
        embed.set_footer(text=author)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(InspireCog(bot))
