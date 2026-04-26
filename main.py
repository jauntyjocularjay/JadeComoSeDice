import os
import logging
import random
import discord
from discord.ext import commands
from dotenv import load_dotenv
from constants import *



load_dotenv()
token = os.getenv(DISCORD_TOKEN)

handler = logging.FileHandler(filename=DSCRD[LOG], encoding=UTF8, mode=W)

description = """ An example bot to showcase the discord.ext.commands extension module.

There are a number of utility commands being showcased here.
"""

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='//', description=description, intents=intents)


@bot.event
async def on_ready():
    # Tell the type checker that User is filled up at this point
    assert bot.user is not None

    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    outcomes = [random.randint(1, limit) for r in range(rolls)]
    total = sum(x for x in outcomes)

    result = f'{ctx.author.mention} rolled `{limit}d{rolls}` for:\n```{outcomes}```\nand a total of `{total}`'
    await ctx.send(result)

@bot.command()
async def Roll(ctx, dice: str):
    await roll(ctx, dice)

@bot.command()
async def ROLL(ctx, dice: str):
    await roll(ctx, dice)

@bot.command()
async def role(ctx, message: str):
    message = message.lower()
    result = f'I couldn\'t find the role in `{message}`.'

    for x,y in D20[FUTURED20][ROLES].items():
        x = x.lower()
        if x in message:
            result = f'Here is the info for the {x} class: {D20_BASE + y}'
            await ctx.send(result)
            break

    await ctx.send(result)

@bot.command()
async def Role(ctx, message: str):
    await role(ctx, message)

@bot.command()
async def roles(ctx, message: str):
    await role(ctx, message)

@bot.command()
async def Roles(ctx, message: str):
    await role(ctx, message)

@bot.command()
async def cybernetics(ctx):
    await ctx.send(f'The Cybernetics Reference: {D20_BASE}{D20[FUTURED20][CYBERNETICS][README]}')

@bot.command()
async def augmentation(ctx):
    await cybernetics(ctx)

@bot.command()
async def augmentations(ctx):
    await cybernetics(ctx)


bot.run(str(token))
