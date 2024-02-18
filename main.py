import asyncio
import discord

import lib.json_handler as json_handler

from discord.ext import commands


class aiodata():
    def __init__(self):
        secrets = json_handler.read_json("secrets/secrets.json")
        self.token = secrets["token"]

        @bot.event
        async def on_ready():
            print("Good morning")
            await self.load_cogs()
            print("Cogs loaded!")

    async def load_cogs(self):
        await bot.load_extension("cogs.pull")

    def run(self):
        bot.run(self.token)
        

if __name__ == "__main__":
    intents = discord.Intents.all()
    bot = commands.Bot(command_prefix='!', intents=intents)

    main = aiodata()
    main.run()