import os
import logging
import random
import re
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
ROLE_SECTIONS = (
    (BASICS, 'Basic Classes'),
    (MODERN, 'Modern Classes'),
    (FUTURE, 'Future Classes'),
    (ARCANA, 'Arcana Classes'),
)

bot = commands.Bot(command_prefix=PREFIX, description=description, intents=intents, case_insensitive=True)

@bot.event
async def on_ready():
    # Tell the type checker that User is filled up at this point
    assert bot.user is not None

    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

def parse_rolls(dice_expression: str):
    """Parse one or more dice expressions into randomized rolls.

    The user can provide either a single entry such as ``2d6`` or a comma-separated
    sequence such as ``2d6, 4d20``. Whitespace is also accepted between entries.

    Args:
        dice_expression: Raw text from the user containing the dice to roll.

    Returns:
        A list of ``(label, outcomes, total)`` tuples. Each entry contains the
        dice notation used, the individual roll results, and the sum of that set.

    Raises:
        ValueError: If the provided expression is empty or contains an invalid dice
            format or non-positive values.
    """
    dice_entries = [part.strip() for part in re.split(r'\s*,\s*|\s+', dice_expression.strip()) if part.strip()]
    if not dice_entries:
        raise ValueError('Format has to be in N(umber of)D(ice)N(umber of sides). Written as NDN or a comma-separated list like `2d6, 4d20`.')

    rolls = []
    for dice_entry in dice_entries:
        try:
            count, sides = dice_entry.lower().split('d')
            count = int(count)
            sides = int(sides)
        except ValueError as exc:
            raise ValueError('Format has to be in N(umber of)D(ice)N(umber of sides). Written as NDN or a comma-separated list like `2d6, 4d20`.') from exc

        if count <= 0 or sides <= 0:
            raise ValueError('Dice values must be positive numbers.')

        outcomes = [random.randint(1, sides) for _ in range(count)]
        total = sum(outcomes)
        rolls.append((f'{count}d{sides}', outcomes, total))

    return rolls

@bot.command(aliases = ['how', 'faq', 'guide', 'comose', 'como-se'])
async def tutorial(ctx, *, user: str = ''):
    target = None
    if ctx.message.mentions:
        target = ctx.message.mentions[0]
    elif user:
        try:
            target = await commands.MemberConverter().convert(ctx, user)
        except commands.BadArgument:
            target = None

    if target is None:
        await ctx.send(f'{ctx.author.mention}, please mention a user in the command, like `//tutorial @username`.')
        return

    user_guide_url = 'https://github.com/jauntyjocularjay/JadeComoSeDice/blob/master/README-User.md'
    message = f'Here is my {link("user guide", user_guide_url)}'

    try:
        await target.send(message)
        await ctx.send(f'{ctx.author.mention}, I sent the guide to {target.mention}.')
    except discord.Forbidden:
        await ctx.send(f'{ctx.author.mention}, I could not send a DM to {target.mention}. Please open the guide here: {user_guide_url}')

@bot.command(aliases = ['r'])
async def roll(ctx, *dice_tokens: str):
    """Roll one or more dice expressions and send each result back to Discord.

    The command accepts a single dice expression such as ``2d6`` or a group like
    ``2d6, 4d20``. Each roll is displayed with its individual outcomes and total.

    Args:
        ctx: The Discord command context.
        *dice_tokens: Raw dice text passed by the user.
    """
    dice_expression = ' '.join(dice_tokens).strip()
    if not dice_expression:
        await ctx.send('Format has to be in N(umber of)D(ice)N(umber of sides). Written as NDN or a comma-separated list like `2d6, 4d20`.')
        return

    try:
        rolls = parse_rolls(dice_expression)
    except ValueError as exc:
        await ctx.send(str(exc))
        return

    result = [ctx.author.mention]
    for roll_name, outcomes, total in rolls:
        result.extend([
            '',
            f'rolled `{roll_name}`',
            '```',
            f'[ {", ".join(str(value) for value in outcomes)} ]',
            f'total = {total}',
            '```',
        ])

    await ctx.send('\n'.join(result))

@bot.command(aliases = ['roles', 'class', 'classes'])
async def role(ctx, message: str = ''):
    if not message:
        await ctx.send(get_role_reference_links())
        return

    for section in (BASICS, MODERN, FUTURE, ARCANA):
        dataset = {
            role_name: f'/{section}/{CLASSES}.md#{parse_index(str(role_name))}'
            for role_name in D20[section].get(ROLES, [])
        }
        result = lookup(D20_BASE, dataset, message, item_name='role', ignore_keys=())
        if 'I couldn\'t find that role' not in result:
            await ctx.send(result)
            return

    await ctx.send(build_not_found_role_message())

@bot.command(aliases = ['equip', 'gear'])
async def equipment(ctx):
    reference = build_reference_url(D20_BASE, FUTURE, D20[FUTURE][EQUIPMENT][INDEX])
    await ctx.send(f'Future Equipment: {link("Future Equipment", reference)}')

@bot.command(aliases = ['aug', 'augmentations', 'augmentation', 'cybernetic'])
async def cybernetics(ctx):
    reference = build_reference_url(D20_BASE, FUTURE, D20[FUTURE][CYBERNETICS][INDEX])
    await ctx.send(f'Take a look at {link("Cybernetics Reference", reference)}')

@bot.command(aliases=['skills'])
async def skill(ctx, message: str = ''):
    reference = build_reference_url(D20_BASE, D20[BASICS][SKILLS][INDEX])
    result = lookup(reference, D20[BASICS][SKILLS], message, item_name='skill', ignore_keys=(INDEX,))
    await ctx.send(result)

@bot.command(aliases = ['beasts', 'animal', 'animals'])
async def beast(ctx, message: str = ''):
    reference = build_reference_url(D20_BASE, D20[BESTIARY][INDEX])
    result = lookup(reference, D20[BESTIARY], message, item_name='beast', ignore_keys=(INDEX, BEASTS))
    await ctx.send(result)

@bot.command(aliases = ['mutations'])
async def mutation(ctx, message: str = ''):
    reference = build_reference_url(D20_BASE, D20[FUTURE][MUTATIONS][INDEX])
    result = lookup(reference, D20[FUTURE][MUTATIONS], message, item_name='mutation', ignore_keys=(INDEX,))
    await ctx.send(result)

def get_role_reference_links():
    return '\n'.join(
        link(title, build_reference_url(D20_BASE, section, D20[section][CLASSES]))
        for section, title in ROLE_SECTIONS
    )

def build_not_found_role_message():
    return (
        f'I couldn\'t find that role. Please check the spelling and try again.\n\n'
        f'Here are the available role categories:\n'
        f'{get_role_reference_links()}\n\n'
        f'Use `{PREFIX}role [name]` to search for a specific role.'
    )

def build_reference_url(*parts: str) -> str:
    return '/'.join(part.strip('/') for part in parts if part)

def lookup(reference: str, dataset: dict, query: str = '', *, item_name: str, ignore_keys=()):
    """Look up an item in a D20 reference dataset and return its markdown anchor link.

    Args:
        reference: The base URL for the reference index page.
        dataset: A dictionary of lookup values keyed by their canonical names, or an iterable
            of (key, value) pairs when a lookup spans multiple sections.
        query: The raw user input to match against the lookup keys.
        item_name: Human-readable label used in failure and success messages.
        ignore_keys: Dataset entries to skip while searching, such as the index key.

    Returns:
        A formatted reference message with either the matching anchor link or a not-found
        message. If the user did not provide a query, the index/reference link is returned.
    """
    if not query:
        return f'Here is the {link(item_name.title(), reference)} reference.'

    normalized_query = parse_index(query)
    result = (
        f'I couldn\'t find that {item_name}. '
        f'Check and see if it is in one of these sections: {link("Mutations", reference)}'
    )

    if isinstance(dataset, dict):
        entries = dataset.items()
    else:
        entries = dataset

    for key, value in entries:
        if key in (INDEX, *ignore_keys):
            continue

        lookup_key = parse_index(str(key))
        if matches_query(normalized_query, lookup_key):
            return f'Here is the info for {link(lookup_key, reference + value)}'

    return result

def matches_query(normalized_query: str, lookup_key: str) -> bool:
    return lookup_key == normalized_query or normalized_query in lookup_key or lookup_key in normalized_query

def parse_index(message: str):
    message = message.lower()
    return message.replace(' ', '-').replace('_', '-')

def link(shown_text: str, url: str):
    return f'[{shown_text}]({url})'

bot.run(str(token))