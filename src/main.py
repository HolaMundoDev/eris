from os import getenv
from discord.ext import commands
import discord
from dotenv import load_dotenv

# Load enviroments from .env file
load_dotenv()

# Create bot client
prefix = getenv("BOT_PREFIX")
description = getenv("BOT_DESCRIPTION")
client = commands.Bot(command_prefix=prefix, description=description)


# On bot ready
@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")


# On member Join
@client.event
async def on_member_join(member):
    messageDescription = f"""
    Hola <{member.mention}>! Bienvenido/a a Hola Mundo, nos complace tenerte en nuestra comunidad, recuerda leer las <#789293321960554517> para evitar ser advertido. Y no olvides pasar por <#789297714101092393> para dar un pequeño resumen sobre ti.
    """
    newUserMessage = discord.Embed(
        title="¡Bienvenido/a al servidor!",
        description=messageDescription,
        color=discord.Color.random(),
    )
    newUserMessage.set_thumbnail(url=member.avatar_url)

    print("Recognised that a member called " + member.name + " joined")
    try:
        channel = client.get_channel(791070017877442600)
        await channel.send(embed=newUserMessage)
        print("Sent message to " + member.name)
    except Exception as err:
        print("Couldn't message " + member.name + "Error: " + err)


# Load the extensions or cogs
cogs = ["cogs.ping"]
for i in cogs:
    try:
        client.load_extension(i)
    except Exception as err:
        print(f"An error has occurred {err}")

# Run the bot
if __name__ == "__main__":
    client.run(getenv("BOT_TOKEN"))
