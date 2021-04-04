from discord.ext import commands
import requests
from os import getenv
from dotenv import load_dotenv
from json import loads
from discord import Embed


class pull(commands.Cog):
    def __init__(self, client):
        self.client = client
        load_dotenv()
        self.bible_token = getenv('BIBLE_TOKEN')

    @commands.command(name='get', aliases=['verse', 'pull', 'retrieve'])
    async def get(self, context, book: str = None, chapter: int = None, verse: int = None):
        if not book:
            response = requests.get(url='https://api.scripture.api.bible/v1/bibles/685d1470fe4d5c3b-01/books', headers={
                'api-key': self.bible_token
            })
            books_json = loads(response.text)['data']
            books = []
            for book in books_json:
                books.append(book['name'])
            embed = Embed(title='Available Books')
            for x in range(0, 12):
                embed.add_field(name=str(x), inline=True, value=books[x])
            message = await context.send(f'{context.author.mention}', embed=embed)
            await message.add_reaction('\U000025b6')
            # wait for either reaction or message sent with book of bible
            # await self.client.wait_for()



def setup(client):
    client.add_cog(pull(client))
