import json
from discord.ext import commands
import discord
from keep_alive import keep_alive

# Load enviroments from .env file
with open("src/credentials.json") as f:
    global data
    data = json.load(f)

# Create bot client
prefix = data["BOT_PREFIX"]
description = data["BOT_DESCRIPTION"]
client = commands.Bot(command_prefix=prefix, description=description, help_command=None)


# On bot ready
@client.event
async def on_ready():
    await client.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            url="https://www.youtube.com/channel/UC4FHiPgS1KXkUMx3dxBUtPg",
            name="Hola Mundo en YouTube",
        )
    )
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
        channel = client.get_channel("791070017877442600")
        await channel.send(embed=newUserMessage)
        print("Sent message to " + member.name)
    except Exception as err:
        print("Couldn't message " + member.name + "Error: " + err)


# Load the extensions or cogs
cogs = [
    "cogs.ping",
    "cogs.avatar",
    "cogs.moderation",
    "cogs.help",
    "cogs.jokes",
    "cogs.cita",
    "cogs.wiki",
    "cogs.npm",
    "cogs.crates",
    "cogs.pypi",
]
for i in cogs:
    try:
        client.load_extension(i)
    except Exception as err:
        print(f"An error has occurred {err}")

keep_alive()
# Run the bot
if __name__ == "__main__":
    client.run(data["BOT_TOKEN"])
