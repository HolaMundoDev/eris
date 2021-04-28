import discord
import requests
from discord.ext import commands


class Synonymous(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="english")
    async def synonymous(self, ctx, *, args):
        req = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en_US/{args}")
        if req.status_code == 200:
            resp = req.json()
            getFirst = resp[0]
            soundsOne = getFirst["phonetics"]
            soundsTuple = soundsOne[0]
            significados = getFirst["meanings"]
            meaningsTuple = significados[0]
            definitions = meaningsTuple["definitions"]
            primerSignificado = definitions[0]
            embed = discord.Embed(
                title="La definción, sinónimos y pronunciación es :flag_um: :flag_gb: :",
                description=f"""
               
                Palabra: {getFirst["word"]}
               
                ** -------PRONUNCIACIÓN------- **

                Texto: {soundsTuple["text"]}
                Audio: {soundsTuple["audio"]}

                ** -------SIGNIFICADOS-------- **

                Parte de la oración: {meaningsTuple["partOfSpeech"]}
                Definición: {primerSignificado["definition"]}
                Sinónimos: {primerSignificado["synonyms"]}
                Ejemplo: {primerSignificado["example"]}
                """,
                color=discord.Color.random(),
            )
            embed.set_thumbnail(
                url="https://media3.giphy.com/media/C6rDaiXF53dJe/giphy.gif?cid=ecf05e474w3i0wb6rtq4iyyrgqvbk08890d0z0p0lqhf5f8l&rid=giphy.gif&ct=g"
            )
            await ctx.send(embed=embed)
        else:
            embedError = discord.Embed(
                title="Error :x:",
                description="API NOT FOUND OR API BAD ERROR",
                color=discord.Color.red(),
            )
            embedError.set_thumbnail(
                url="https://media1.tenor.com/images/46ce1235c5697ce170c6e84f4b4fb4e7/tenor.gif"
            )
            await ctx.send(embed=embedError)


def setup(bot):
    bot.add_cog(Synonymous(bot))
