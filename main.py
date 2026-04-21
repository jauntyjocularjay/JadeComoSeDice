import random as Random
import discord as Discord
import logging
import os
from discord.ext import commands
from dotenv import load_dotenv

true = True
false = False

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = Discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='/', intents=intents)

def roll(dice: str = 1d6):
    

@bot.event
async def on_ready():
    print(f"We are ready to go in, {bot.user.name}")

@bot.event
async def on_message(message):
    pass

@bot.command()
async def roll(ctx, *, message):
    pass

@secret.error
async def error(ctx, error):
    pass

bot.run(token, log_handler=handler, log_level=logging.DEBUG)