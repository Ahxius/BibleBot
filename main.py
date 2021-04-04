import os
from dotenv import load_dotenv
from discord import Intents
from discord.ext.commands import Bot

load_dotenv()
discord_token = os.getenv('DISCORD_TOKEN')
bible_token = os.getenv('BIBLE_TOKEN')
intents = Intents.default()


client = Bot(command_prefix='b!', intents=intents)

for module in os.listdir('modules'):
    if not module.endswith('.py'):
        continue
    try:
        client.load_extension(f'modules.{module[:-3]}')
    except SyntaxError as es:
        print(f'Failed to load module {module} due to a syntax error.')
    except ImportError as es:
        print(f'Failed to load module {module} due to an import error.')


@client.event
async def on_ready():
    print(f'Discord login successful - {client.user}')


client.run(discord_token)
