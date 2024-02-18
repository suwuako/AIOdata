import asyncio

from discord import app_commands
from discord.ext import commands

class pull(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="pull", description="pulls da data")
    async def pull(interaction, message):
        secrets = json_handler.read_json("secrets/secrets.json")
        perms = secrets["perms"]

        if interaction.message.author.id not in perms:
            await interaction.response.send_message("get outta here")
            return

        print(f"Poll requested for f{interaction.channel}")
        channel = interaction.channel 
        counter = 0

        now = datetime.now()
        await interaction.response.send_message(f"Polling results: (starting {now})")
        
        async for message in channel.history(limit=1000):
            # message.content, message.author.id, 
            print(message.content)
            counter += 1
        
        done = datetime.now()
        await interaction.followup.send(f"done (timedelta of {done - now}) of {counter} objects")

async def setup(bot):
    await bot.add_cog(pull(bot))
