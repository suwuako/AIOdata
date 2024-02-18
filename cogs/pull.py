import asyncio
import discord
from datetime import datetime

import lib.json_handler as json_handler

from discord import app_commands
from discord.ext import commands

class pull(commands.Cog):
    group = app_commands.Group(name='data', description="data utility stuff")
    def __init__(self, bot):
        self.bot = bot

    @group.command(name="pull", description="pulls da data")
    async def pull(self, interaction):
        secrets = json_handler.read_json("secrets/secrets.json")
        perms = secrets["perms"]
        out = {}
        objects = 50000

        if interaction.user.id not in perms:
            print(interaction.user.id)
            await interaction.response.send_message("get outta here (no perms)")
            return

        print(f"Poll requested for {interaction.channel}")
        channel = interaction.channel 
        counter = 0

        now = datetime.now()
        await interaction.response.send_message(f"Polling {objects} results: (starting {now})")
        
        async for message in channel.history(limit=objects):
            # message.content, message.author.id, 
            content = message.content.upper().split()
            userid = message.author.id

            if userid == self.bot.user.id:
                pass

            if userid not in out.keys():
                out[userid] = {}

            for word in content:
                if word not in out[userid].keys():
                    out[userid][word] = 1
                else:
                    out[userid][word] += 1

            counter += 1
        
        done = datetime.now()
        await interaction.followup.send(f"Polling done (timedelta of {done - now}) of {counter} objects")
        print(out)

        for userid in out.keys():
            top_word = ''
            count = 0
            for k, v in out[userid].items():
                if v > count:
                    count = v
                    top_word = k

            user = self.bot.get_user(userid)

            try:
                await interaction.followup.send(f"`top word for {user.name} is {top_word} with a count of {count}`")
            except:
                pass

        json_handler.write_json("secrets/data.json", out)

async def setup(bot):
    await bot.add_cog(pull(bot))
