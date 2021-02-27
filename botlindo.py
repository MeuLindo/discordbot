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
    
    await send_message.add_reaction('🤖')
    
@bot.command(name='qc')
async def quarentena_gaming(ctx):
    choose = random.choice(qc)
    send_message = await ctx.send(choose)
    await send_message.add_reaction('🦑')

@bot.command(name='smoke')
async def quarentena_gaming(ctx):
    await ctx.send('Essa smoke aí é pra ganhar espaço')

@bot.command(name='bomb')
async def quarentena_gaming(ctx):
    await ctx.send('O que acontece no bomb fica no bomb.')
    
@bot.command(name='flash')
async def quarentena_gaming(ctx):
    await ctx.send('Pode ir que eu tenho a perfeitinha.')

@bot.command(name='spray')
async def quarentena_gaming(ctx):
    await ctx.send('Tarik do céu!')

@bot.command(name='noscope')
async def quarentena_gaming(ctx):
    await ctx.send('https://www.youtube.com/watch?v=kBN7T5V-yGk')


bot.run(TOKEN)
