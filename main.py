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

bot = commands.Bot(command_prefix='//', description=description, intents=intents, case_insensitive=True)

@bot.event
async def on_ready():
    # Tell the type checker that User is filled up at this point
    assert bot.user is not None

    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

@bot.command(aliases = ['r'])
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in N(umber of)D(ice)N(umber of sides). Written as NDN.')
        return

    outcomes = [random.randint(1, limit) for r in range(rolls)]
    total = sum(x for x in outcomes)

    result = f'{ctx.author.mention} rolled `{limit}d{rolls}` for:\n```{outcomes}```\nand a total of `{total}`'
    await ctx.send(result)

@bot.command(aliases = ['class'])
async def role(ctx, message: str):
    message = message.lower()
    
    link = f'{D20_BASE}/{FUTURE}/{D20[FUTURE][INDEX]}'

    result = f'I couldn\'t find the class in `{message}`. Try checking these out: FutureD20 Classes {link}.'

    for x,y in D20[FUTURE][CLASSES].items():
        x = x.lower()
        if x in message:
            result = f'Here is the info for the {x} class: {link}{y}'
            break

    await ctx.send(result)

@bot.command(aliases = ['classes'])
async def roles(ctx):
    result = f'Future D20 classes: {D20_BASE}/{FUTURE}/{D20[FUTURE][CLASSES][INDEX]}'
    await ctx.send(result)

@bot.command(aliases = ['equip'])
async def equipment(ctx):
    result = f'FutureD20 Equipment: {D20_BASE}/{FUTURE}/{D20[FUTURE][EQUIPMENT]}'
    await ctx.send(result)

@bot.command(aliases = ['augmentations', 'augmentation', 'cybernetic'])
async def cybernetics(ctx):
    await ctx.send(f'Take a look at Cybernetics Reference: \n{D20_BASE}/{FUTURE}/{D20[FUTURE][CYBERNETICS][INDEX]}')

@bot.command()
async def skills(ctx):
    
    link = D20_BASE + D20[SKILLS][INDEX]
    
    await ctx.send(f'Here is the skill reference:\n{link}')

@bot.command()
async def skill(ctx, message):
    message = message.lower()

    link = f'{D20_BASE}/{SKILLS}'

    result = f'I couldn\'t find that skill. Check and see if it is in one of these sections: {link}'

    for x,y in D20[SKILLS].items():
        x = x.lower()
        if x in message:
            result = f'Here is the info for the {x} skill: {link + y}'
            break
    
    await ctx.send(result)

bot.run(str(token))
