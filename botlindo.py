import os
import random
from dotenv import load_dotenv
from discord.ext import commands
import discord

from qi_quotes import quotes
from qc_quotes import qc

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.command(name='qi')
async def quite_interesting(ctx):
    
    choose = random.choice(quotes)
    author = '**' + choose['Author'] + ':**'
    quote = '*' + choose['Quote'] + '*'
    episode = '- Ep: ' + choose['EP']
    send_message = await ctx.send(author + '\n' + quote + '\n' + episode)
    
    emoji = '\N{THUMBS UP SIGN}'
    await send_message.add_reaction(emoji)
    
@bot.command(name='qc')
async def quarentena_gaming(ctx):
    choose = random.choice(qc)
    send_message = await ctx.send(choose)

@bot.command(name='smoke')
async def quarentena_gaming(ctx):
    await ctx.send('Essa smoke aí é pra ganhar espaço')

@bot.command(name='bomb')
async def quarentena_gaming(ctx):
    await ctx.send('O que acontece no bomb fica no bomb.')


bot.run(TOKEN)
