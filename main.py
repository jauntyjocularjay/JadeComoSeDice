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

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f"We are ready to go in, {bot.user.name}")

@bot.command
async def roll(ctx, *, dice: str = '1d6'):
    d_index = dice.index('d')

    number_of_dice_as_string = dice[:d_index]
    number_of_sides_as_string = dice[d_index+1:]

    number_of_dice = int(number_of_dice_as_string)
    number_of_sides = int(number_of_sides_as_string)

    result = [Random.randint(1,number_of_sides) for _ in range(number_of_dice)]
    total = sum(x for x in result)

    await ctx.send(f'{ctx.author.mention} rolled {number_of_dice} d{number_of_sides} for:\n    {result}\n    and a total of {total}')

bot.run(token, log_handler=handler, log_level=logging.DEBUG)
