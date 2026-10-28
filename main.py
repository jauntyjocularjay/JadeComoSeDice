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

PREFIX = '//'

bot = commands.Bot(command_prefix=PREFIX, description=description, intents=intents, case_insensitive=True)

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

@bot.command(aliases = ['roles', 'class', 'classes'])
async def role(ctx, message: str = ''):
    basic_classes = f'{D20_BASE}/{BASICS}/{D20[BASICS][CLASSES]}'
    modern_classes = f'{D20_BASE}/{MODERN}/{D20[MODERN][CLASSES]}'
    future_classes = f'{D20_BASE}/{FUTURE}/{D20[FUTURE][CLASSES]}'
    arcana_classes = f'{D20_BASE}/{ARCANA}/{D20[ARCANA][CLASSES]}'

    if not message:
        result = f'Basic Classes: {basic_classes} \n' + f'Modern Classes: {modern_classes} \n' + f'Future Classes: {future_classes} \n' + f'Arcana Classes: {arcana_classes}'
        await ctx.send(result)
        return

    normalized_message = parse_index(message)
    sets = [BASICS, MODERN, FUTURE, ARCANA]

    for set in sets:
        dataset = D20[set].get(ROLES, [])
        for role in dataset:
            if parse_index(str(role)) == normalized_message:
                role_link = f'{D20_BASE}/{set}/{CLASSES}.md#{normalized_message}'
                await ctx.send(role_link)
                return

    not_found_message = (
        f'I couldn\'t find that role. Please check the spelling and try again.\n\n'
        f'Here are the available role categories:\n'
        f'**Basic Classes:** {basic_classes}\n'
        f'**Modern Classes:** {modern_classes}\n'
        f'**Future Classes:** {future_classes}\n'
        f'**Arcana Classes:** {arcana_classes}\n\n'
        f'Use `{PREFIX}role [name]` to search for a specific role.'
    )
    await ctx.send(not_found_message)

@bot.command(aliases = ['equip'])
async def equipment(ctx):
    result = f'Future Equipment: {D20_BASE}/{FUTURE}/{D20[FUTURE][EQUIPMENT][INDEX]}'
    await ctx.send(result)

@bot.command(aliases = ['augmentations', 'augmentation', 'cybernetic'])
async def cybernetics(ctx):
    await ctx.send(f'Take a look at Cybernetics Reference: \n{D20_BASE}/{FUTURE}/{D20[FUTURE][CYBERNETICS][INDEX]}')

def lookup(reference: str, dataset: dict, query: str = '', *, item_name: str, ignore_keys=()):
    """Look up an item in a D20 reference dataset and return its markdown anchor link.

    Args:
        reference: The base URL for the reference index page.
        dataset: A dictionary of lookup values keyed by their canonical names.
        query: The raw user input to match against the lookup keys.
        item_name: Human-readable label used in failure and success messages.
        ignore_keys: Dataset entries to skip while searching, such as the index key.

    Returns:
        A formatted reference message with either the matching anchor link or a not-found
        message. If the user did not provide a query, the index/reference link is returned.
    """
    if not query:
        return f'Here is the {item_name} reference:\n{reference}'

    normalized_query = parse_index(query)
    result = f'I couldn\'t find that {item_name}. Check and see if it is in one of these sections: {reference}'

    for key, value in dataset.items():
        if key in (INDEX, *ignore_keys):
            continue

        lookup_key = parse_index(str(key))
        if lookup_key == normalized_query or normalized_query in lookup_key or lookup_key in normalized_query:
            return f'Here is the info for the {lookup_key} {item_name}: {reference + value}'

    return result

@bot.command(aliases=['skills'])
async def skill(ctx, message: str = ''):
    link = f'{D20_BASE}/{D20[BASICS][SKILLS][INDEX]}'
    result = lookup(link, D20[BASICS][SKILLS], message, item_name='skill', ignore_keys=(INDEX,))
    await ctx.send(result)

@bot.command(aliases = ['beasts', 'animal', 'animals'])
async def beast(ctx, message: str = ''):
    link = f'{D20_BASE}/{D20[BESTIARY][INDEX]}'
    result = lookup(link, D20[BESTIARY], message, item_name='beast', ignore_keys=(INDEX, BEASTS))
    await ctx.send(result)

@bot.command(aliases = ['mutations'])
async def mutation(ctx, message: str = ''):
    link = f'{D20_BASE}{D20[FUTURE][MUTATIONS][INDEX]}'
    result = lookup(link, D20[FUTURE][MUTATIONS], message, item_name='mutation', ignore_keys=(INDEX,))
    await ctx.send(result)

def parse_index(message: str):
    message = message.lower()
    return message.replace(' ', '-').replace('_', '-')

bot.run(str(token))
