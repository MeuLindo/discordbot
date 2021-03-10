import os
import random
from dotenv import load_dotenv
from discord.ext import commands
import discord
import requests
import xml.etree.ElementTree as ET
import html2text
import json


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


def getBitcoinPrice():
    
    S = requests.Session()

    URLCURRENCY = "http://api.currencylayer.com/live?access_key=3096802859eab4748db45256d2c3aed1&format=1"

    R = S.get(URLCURRENCY)
    DATA = json.loads(R.content)
    USDBRL = DATA["quotes"]["USDBRL"]
    USDBTC = DATA["quotes"]["USDBTC"]

    BTCBRL = (1/USDBTC) * USDBRL
    formatacaoBTCBRL = '{:.}'.format(round(BTCBRL))

    return formatacaoBTCBRL

def getLitecoinPrice():
    
    S = requests.Session()

    URLCURRENCY = "http://api.currencylayer.com/live?access_key=3096802859eab4748db45256d2c3aed1&format=1"
    R = S.get(URLCURRENCY)
    DATA = json.loads(R.content)
    USDBRL = DATA["quotes"]["USDBRL"]
    
    URLLITECOIN = "https://www.litecoinpool.org/api?api_key=7f9cdb6341bea09d18cb8979fc57846d"
    LR = S.get(URLLITECOIN)
    LITEDATA = json.loads(LR.content)
    LTCUSD = LITEDATA["market"]["ltc_usd"]

    LTCBRL = LTCUSD * USDBRL
    formatacaoLTCBRL = '{:.}'.format(round(LTCBRL))
    
    return formatacaoLTCBRL


bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.command(name='bitcoin')
async def quite_interesting(ctx):
    bitHoje = getBitcoinPrice()
    send_message = await ctx.send(f'**R${bitHoje}**')

@bot.command(name='litecoin')
async def quite_interesting(ctx):
    liteHoje = getLitecoinPrice()
    send_message = await ctx.send(f'**R${liteHoje}**')


@bot.command(name='hoje')
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
    
@bot.command(name='qc', brief='Pega uma quote aleatória e lê ela em TTS.')
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

@bot.command(name='noscope', brief='Video do Meu Lindo.')
async def quarentena_gaming(ctx):
    await ctx.send('https://www.youtube.com/watch?v=kBN7T5V-yGk')

@bot.command(name='bala')
async def quarentena_gaming(ctx):
    await ctx.send('*INVOCANDO* - @everyone', tts=True)

bot.lobby = '**Lobby**:'

@bot.command(name='lobby', brief='Cria um lobby [!lobby (jogador1 jogador2 ...)]')
async def quarentena_gaming(ctx, *players):
    bot.lobby += '\n'.join(players) + '\n'
    await ctx.send(bot.lobby)


@bot.command(name='presente', brief='Se coloca no lobby criado.')
async def quarentena_gaming(ctx):
    user = str(ctx.author)
    nome = '\n' + user.split('#')[0] 
    if nome in bot.lobby:
        await ctx.send(bot.lobby)
    else:
        bot.lobby += nome
        await ctx.send(bot.lobby)

@bot.command(name='resetlobby', brief='Reinicia a lista do lobby.')
async def quarentena_gaming(ctx):
    bot.lobby = '**Lobby**:'
    await ctx.send('Lobby foi resetado.')

@bot.command(name='quote', brief='Adiciona uma quote da lista.')
async def quarentena_gaming(ctx, *quote_msg):
    
    quote = ' '.join(quote_msg)

    if quote in qc:
        await ctx.send('Quote já ta na lista.')
    else:
        qc.append(quote)    
    
        with open('qc_quotes.py', 'w') as f:
            f.write(f"qc = {str(qc)}")
        
        await ctx.send('Quote Adicionada.')

@bot.command(name='rmquote', brief='Remove uma quote da lista.')
async def quarentena_gaming(ctx, *quote_msg):
    
    quote = ' '.join(quote_msg)

    for item in qc:
        achei = 0
        if item == quote:
            qc.remove(item)
            with open('qc_quotes.py', 'w') as f:
                f.write(f"qc = {str(qc)}")
            
            achei = 1
            await ctx.send('Quote Removida.')
        else:
            achei = 0
    
    if not achei:
        await ctx.send('Quote não ta na lista.')

bot.run(TOKEN)



getWikiDay()