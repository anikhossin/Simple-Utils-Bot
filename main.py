import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from logging_config import setup_logging    
import logging

setup_logging()

load_dotenv()

async def load_commands(bot):
    for folder in os.listdir('./src'):
        if os.path.isdir(f'./src/{folder}'):
            for file in os.listdir(f'./src/{folder}'):
                if file.endswith('.py'):
                    try:
                        await bot.load_extension(f'src.{folder}.{file[:-3]}')
                        logging.debug(f"Successfully loaded {file}")
                    except Exception as e:
                        logging.error(f"Failed to load {file}: {e}")

class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=os.getenv('PREFIX'), intents=discord.Intents.all(), help_command=None)
        
    async def on_ready(self):
        logging.info(f'Logged in as {self.user}')
        await load_commands(self)

bot = MyBot()

if __name__ == '__main__':
    bot.run(os.getenv('TOKEN'))
