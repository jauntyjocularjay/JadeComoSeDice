# Jade's D20 Reference Bot

A Discord bot that links to FutureD20 rules content and includes a simple dice roller.

## Current Implementation

- Language: Python 3
- Framework: `discord.py`
- Prefix: `//`
- Token source: environment variable `DISCORD_TOKEN`
- Log file: `discord.log` (overwritten each run)

## Setup

1. Create and activate a virtual environment.
2. Install dependencies.
3. Set `DISCORD_TOKEN` in your environment or a `.env` file.
4. Run the bot.

Example:

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements
touch .env
echo "DISCORD_TOKEN=your_token_here" > .env
python main.py
```

## Commands

All commands use the `//` prefix.

### Dice

- `//roll NdN`
- Aliases: `//Roll`, `//ROLL`
- Example: `//roll 2d6`
- Input must be in `NdN` format.

### FutureD20 Class Lookup

- `//role <text>`
- Aliases: `//Role`, `//roles <text>`, `//Roles <text>`
- Matches if a class name is contained inside `<text>` (case-insensitive).
- Returns the class markdown link from the FutureD20 Classes section.
- If no match is found, returns a fallback link to the classes index.

#### Currently Mapped FutureD20 Classes

Ambassador, Dogfighter, Dreadnaught, Engineer, Explorer, FieldOfficer, HelixWarrior, MechaJockey, SpaceMonkey, Swindler, Technosavant, Tracer, Xenophile

### Cybernetics Reference

- `//cybernetics`
- Aliases: `//augmentation`, `//augmentations`
- Returns the FutureD20 cybernetics reference link.

### Skills Index

- `//skills`
- Alias: `//Skills`
- Future skills index link
- Placeholder labels for Modern, Arcana, and Menaces (no links yet)

### Specific Skill Lookup

- `//skill <text>`
- Alias: `//Skill <text>`
- Matches known FutureD20 skills by substring (case-insensitive).
- Returns a deep link to the skill anchor in `FutureD20/Skills.md`.
- If no match is found, returns a fallback link to the Future skills index.

#### Currently Mapped FutureD20 Skills

Bluff, Computer Use, Disable Device, Technology, Navigate, Pilot, Repair, Treat Injury

## Notes

- The command aliases are implemented as separate commands in code.
- The `roles` and `Roles` aliases currently require an argument, same as `role`.
- Only FutureD20 links are currently implemented in bot responses.
