import asyncio
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

from cogs import on_messages

load_dotenv()

try:
    load_config = os.getenv("TOKEN")
    print(f'Token retrieved from env')
    intents = discord.Intents.default()
    intents.message_content = True
    intents.messages = True
    bot_instance = commands.Bot(intents=intents, command_prefix="!")
    print("No error raised on login, starting...")
except Exception as e:
    print(e)


async def main():
    @bot_instance.command()
    async def on_message(message):
        print(message)
        await bot_instance.process_commands(message)

    async with bot_instance:
        await bot_instance.add_cog(on_messages.NameCommands(bot_instance))
        await bot_instance.start(os.getenv("TOKEN"))


asyncio.run(main())
