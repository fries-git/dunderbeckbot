import discord
import os
import dotenv

dotenv.load_dotenv()
TOKEN = os.getenv("token")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author.bot:
        return
    content = message.content.lower()
    if "what" in content and "dunderbeck" in content:
        await message.channel.send("[Dunderbeck](https://store.steampowered.com/app/2477750/Dunderbeck/) is the newest game by RustLTD that's an inventory management auto-battler!")

client.run(TOKEN)