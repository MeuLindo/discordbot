import os
import random
from dotenv import load_dotenv
from discord.ext import commands
import discord
import requests
import xml.etree.ElementTree as ET
import html2text


from qi_quotes import quotes
from qc_quotes import qc

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')



def getWikiDay():
    
    S = requests.Session()

    URL = "https://en.wikipedia.org/w/api.php?action=featuredfeed&format=json&feed=onthisday&utf8=1"

    R = S.get(URL)
    DATA = R.content
    root = ET.fromstring(DATA)
    
    onThisDay = root[0][15][0].text
    rawHtml = onThisDay = root[0][15][3].text

    h = html2text.HTML2Text()
    h.ignore_links = True
    parsedHtml = h.handle(rawHtml)
    cut = parsedHtml.split('More anniversaries:')[0]
    
    return cut

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.command(name='hoje', help="")
async def quite_interesting(ctx):
    wikiHoje = getWikiDay()
    send_message = await ctx.send(wikiHoje)
    
    await send_message.add_reaction('🤖')


@bot.command(name='qi')
async def quite_interesting(ctx):
    
    choose = random.choice(quotes)
    author = '**' + choose['Author'] + ':**'
    quote = '*' + choose['Quote'] + '*'
    episode = '- Ep: ' + choose['EP']
    send_message = await ctx.send(author + '\n' + quote + '\n' + episode, tts=True)
    
    await send_message.add_reaction('🤖')
    
@bot.command(name='qc')
async def quarentena_gaming(ctx):
    choose = random.choice(qc)
    send_message = await ctx.send(choose, tts=True)
    await send_message.add_reaction('🦑')

@bot.command(name='smoke')
async def quarentena_gaming(ctx):
    await ctx.send('Essa smoke aí é pra ganhar espaço.', tts=True)

@bot.command(name='bomb')
async def quarentena_gaming(ctx):
    await ctx.send('O que acontece no bomb fica no bomb.', tts=True)
    
@bot.command(name='flash')
async def quarentena_gaming(ctx):
    await ctx.send('Pode ir que eu tenho a perfeitinha.', tts=True)

@bot.command(name='spray')
async def quarentena_gaming(ctx):
    await ctx.send('Tarik do céu!', tts=True)

@bot.command(name='noscope')
async def quarentena_gaming(ctx):
    await ctx.send('https://www.youtube.com/watch?v=kBN7T5V-yGk')

@bot.command(name='bala')
async def quarentena_gaming(ctx):
    await ctx.send('*INVOCANDO* - @everyone', tts=True)

bot.lobby = '**Lobby**:'

@bot.command(name='lobby')
async def quarentena_gaming(ctx, *players):
    bot.lobby += '\n'.join(players) + '\n'
    await ctx.send(bot.lobby)


@bot.command(name='presente')
async def quarentena_gaming(ctx):
    user = str(ctx.author)
    nome = '\n' + user.split('#')[0] 
    if nome in bot.lobby:
        await ctx.send(bot.lobby)
    else:
        bot.lobby += nome
        await ctx.send(bot.lobby)

@bot.command(name='resetlobby')
async def quarentena_gaming(ctx):
    bot.lobby = '**Lobby**:'
    await ctx.send('Lobby foi resetado.')

bot.run(TOKEN)



getWikiDay()