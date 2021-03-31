from os import getenv
from discord import Client
from dotenv import load_dotenv


# Load enviroments from .env file
load_dotenv()

# Create bot client
client = Client()


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!hello"):
        await message.channel.send("Hello!")


if __name__ == "__main__":
    client.run(getenv("BOT_TOKEN"))
