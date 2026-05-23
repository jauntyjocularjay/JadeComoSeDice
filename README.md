# Jade's D20 Reference Bot

Discord bot for quick Future D20 reference links plus a dice roller.

## Current Functionality

- Language: Python 3
- Framework: discord.py commands extension
- Prefix: //
- Case-insensitive commands: enabled
- Token source: DISCORD_TOKEN environment variable (dotenv supported)
- Log file: discord.log

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
python -m main
```

## Commands

All commands use the `//` prefix.

### Dice

- `//roll NdN`
- Aliases: `//Roll`, `//ROLL`
- Example: `//roll 2d6`
- Input must be in `NdN` format.

### role

- Syntax: `//role [text]`
- Alias: `//class`
- Performs case-insensitive substring matching across mapped Future D20 classes.
- Returns the first matching class anchor in Classes.md.
- If no class matches, returns the Future D20 classes index link.

### roles

- Syntax: `//roles`
- Alias: `//classes`
- Returns the Future D20 classes index link.

### equipment

- Syntax: `//equipment`
- Alias: `//equip`
- Returns the Future D20 equipment link.

### cybernetics

- Syntax: `//cybernetics`
- Aliases: `//augmentations`, `//augmentation`, `//cybernetic`
- Returns the Future D20 cybernetics link.

### skills

- `//skills`
- Alias: `//Skills`
- provides the Future skills index link
- Placeholder labels for Modern, Arcana, and Menaces (no links yet)

### Specific Skill Lookup

- Syntax: `//skill [text]`
- Performs case-insensitive substring matching across mapped skills.
- Returns the first matching skill anchor.
- If no skill matches, returns a fallback Skills section link.

## Link Mapping Scope

- Future D20 classes: mapped to Classes.md anchors.
- Future D20 mutations: mapped to Mutations.md anchors in constants.
- Skills: mapped to Skills.md anchors.

## Notes

- Link strings are composed from constants.py and may include extra slash characters depending on stored path fragments.
- Matching behavior is substring-based, so shorter inputs can match multiple keys and return the first hit.
