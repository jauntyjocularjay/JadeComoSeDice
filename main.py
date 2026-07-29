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

description = """ A bot to serve information from the D20 Resources SRT """

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

    result = f'{ctx.author.mention} rolled `{rolls}d{limit}` for:\n```{outcomes}```\nand a total of `{total}`'
    await ctx.send(result)

@bot.command(aliases = ['classes'])
async def roles(ctx):
    basic_classes = f'{D20_BASE}/{BASICS}/{D20[BASICS][CLASSES]}'
    modern_classes = f'{D20_BASE}/{MODERN}/{D20[MODERN][CLASSES]}'
    future_classes = f'{D20_BASE}/{FUTURE}/{D20[FUTURE][CLASSES]}'
    arcana_classes = f'{D20_BASE}/{ARCANA}/{D20[ARCANA][CLASSES]}'

    result = f'Basic Classes: {basic_classes} \n' + f'Modern Classes: {modern_classes} \n' + f'Future Classes: {future_classes} \n' + f'Arcana Classes: {arcana_classes}'
    await ctx.send(result)

@bot.command(aliases = ['class'])
async def role(ctx, message: str):
    message = parse_index(message)
    link = f'{D20_BASE}/set/{CLASSES}.md'
    sets = [BASICS, MODERN, FUTURE, ARCANA]

    for set in sets:
        print(f'checking {set} for {message}')
        if(D20[set][ROLES].count(message) != 0):
            link = f'{D20_BASE}/{set}/{CLASSES}.md#' + message
            print(link)
            await ctx.send(link)
            return

    await roles(ctx)

@bot.command(aliases = ['equip'])
async def equipment(ctx):
    result = f'Future Equipment: {D20_BASE}/{FUTURE}/{D20[FUTURE][EQUIPMENT][INDEX]}'
    await ctx.send(result)

@bot.command(aliases = ['augmentations', 'augmentation', 'cybernetic'])
async def cybernetics(ctx):
    await ctx.send(f'Take a look at Cybernetics Reference: \n{D20_BASE}/{FUTURE}/{D20[FUTURE][CYBERNETICS][INDEX]}')

@bot.command()
async def skills(ctx):
    link = D20_BASE + D20[SKILLS][INDEX]
    
    await ctx.send(f'Here is the skill reference:\n {link}')

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

@bot.command()
async def mutations(ctx):

    link = D20_BASE + D20[FUTURE][MUTATIONS][INDEX]

    await ctx.send(f'Here is the mutations reference:\n{link}')

@bot.command()
async def mutation(ctx, message):
    message = parse_index(message)
    print(f'message: {message}')

    link = D20_BASE + D20[FUTURE][MUTATIONS][INDEX]
    print(f'Link: {link}')

    if(D20[FUTURE][MUTATION].count(message) != 0):
        await ctx.send(f'{link}#{message}')
        return

    await ctx.send(mutations)

def parse_index(message: str):
    message = message.lower()
    return message.replace(' ', '-').replace('_', '-')

bot.run(str(token))
