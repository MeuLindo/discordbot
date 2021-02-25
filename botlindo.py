import os
import random
from dotenv import load_dotenv
from discord.ext import commands

from qi_quotes import quotes

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.command(name='qi')
async def quite_interesting(ctx):
    
    choose = random.choice(quotes)
    author = '**' + choose['Author'] + ':**'
    quote = '*' + choose['Quote'] + '*'
    await ctx.send(author + '\n' + quote)
    

bot.run(TOKEN)