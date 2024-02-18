import discord

from discord import app_commands
from discord.ext import commands


intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)
tree = app_commands.CommandTree(bot)

@bot.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=997168970044014682))
    print("hi")

@bot.event
async def on_message(message):
    print(f"{message.author.id}, {message.content}")

@tree.command(
    name="pull",
    description="pulls",
    guild=discord.Object(id=997168970044014682)
)
async def pull(interaction):
    print("interacted")

bot.run(token)