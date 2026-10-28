# Jade's D20 Reference Bot

Discord bot for quick Future D20 reference links plus a dice roller. Visit the [user guide](./README-User.md).

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

## Link Mapping Scope

- Future D20 classes: mapped to Classes.md anchors.
- Future D20 mutations: mapped to Mutations.md anchors in constants.
- Skills: mapped to Skills.md anchors.

## Notes

- Link strings are composed from constants.py and may include extra slash characters depending on stored path fragments.
- Matching behavior is substring-based, so shorter inputs can match multiple keys and return the first hit.
