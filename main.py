### READ ME ### 
# IMPORTANT: You must run the bot by being on the main file
# then running else if you try running the bot in a cog, it will not start.
#
# HI, So i re created your whole bot, don't know what your bot is called
# so i just called this project (NoobsBot) im asuming you know how to
# rename files/projects ect... anyways every single comment you can
# delete if you want or keep. I suggest you save comments so that you
# can use it as later refrenece, This whole top msg can be deleted.
# PS: You are going to need to download some moudles if you do not have them
# i'll try giving you the commands assuming you know how to install moudles,
# its the same way you had to install the discord moudle. any more help lmk
# - Skely :)

# NOTE: ANYTHING THAT ONLY USES @Client and not @Commands, such as your meme, must be put here in the main file.
### End ###

import discord
import random
import os
from discord.ext import tasks
from discord.ext import commands
from dotenv import load_dotenv # Moudle: py -m pip install python-dotenv

# Grabs Token from .env | This stops your token from getting taken & leaked by hackers
# Note: Do Not add anything else to the .env file else it will error
load_dotenv()
Token = os.getenv('DISCORD_TOKEN')

client = commands.Bot(command_prefix="=")
# Disables default help command
client.remove_command("help")

# Optional welcome on console
print('Welcome name here')

# Creates a new cog | cog is a extension file, it helps to organize
# Read More: https://discordpy.readthedocs.io/en/stable/ext/commands/cogs.html

# Note, Create cogs in the folder nammed "cogs" find it in solution explorer
# Steps, "cogs" folder>Right Click>Add>New Item...>Empty Python File>Name it name then add .py
# example, Skely.py Then add to the extentions
# example
# extensions = ['cogs.help', # MAKE SURE U ADD A , (Comma)
#              'cogs.moderation',
#              'cogs.Skely.py'] # THE LAST COG DOES NOT NEED TO HAVE A COMMA

# To set up a cog, head over to help.py where i show you how.

extensions = ['cogs.help',
              'cogs.moderation',
              'cogs.fun',
              'cogs.eventhandler',
              'cogs.meme',
              'cogs.games',
              'cogs.report']

# Loads cogs when running
if __name__ == '__main__':
    for extension in extensions:
        client.load_extension(extension)

# Loads bot
@client.event
async def on_ready():
    # Shows username
    print(f'logged in as: {client.user.name}')
    # Shows bot
    print(f"Connected to {client.user}")
    # Shows how many servers your bot is in
    print(f"serving in {len(client.guilds)} servers")

# Runs bot with token
client.run(Token)