
# Development Guide

## Using PyScripts

@jauntyjocularjay wrote PyScripts to simplify this process. 

1. run `source pydevstart-**`, replace `**` with your local environment to choose the appropriate script.
    - Sets up the Python Virtual Environent
    - Runs the `activate` script
    - Installs pip from the `requirements` files 
1. Set up the `.env` files
    - Copy `.env.template` to `.env`
    - Paste in your API key for Discord
1. Ensure the bot is not currently running on a server
1. run the bash script `runlocally` to test the functionality
1. merge changes
1. Push changes to GitHub

## Using GitBash

1. Run `python3 -m venv venv` to set up the virtual environment
1. Run `source ./venv/scripts/activate` to run the `activate` script
1. run `pip install -r requirements` to install pips from `requirements`






