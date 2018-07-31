
# 2018 Emir Erbasan (humanova)
# MIT License, see LICENSE for more details

# kareliBot 

# 112 Turnuva Sunucusu'ndaki goeo_ Feed The Beast sunucusu icin yazdigim...
# server kontrol botu

import os,sys
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import re
import minestat

################################

Client = discord.Client()
client = commands.Bot(command_prefix = "!")

version = "kareliBot v0.1\n31.07.18"
myID = "213262071050141696"
botID = "473890180215078925"
mcIconURL = "http://s857.photobucket.com/user/TangentSystem/media/MCicon2.png.html?t=1262414710"

def yaziDuzelt(yazi):
    return int(''.join(list(filter(str.isdigit, yazi))))

@client.event
async def on_ready():
    print("Bot hazir!\n")
    print("%s adiyla giris yapildi" % (client.user.name))
    await client.change_presence(game=discord.Game(name="Meincraft"))

@client.event
async def on_message(message):

    if not message.author.bot == 1:
        
        if message.content.upper() == "!MC" or message.content.upper() == "!FTB":
            
            ms = minestat.MineStat('genco.me', 25565)
            if ms.online:
                ms.version = yaziDuzelt(str(ms.version))
                ms.current_players = yaziDuzelt(str(ms.current_players))
                ms.max_players = yaziDuzelt(str(ms.max_players))

                if str(ms.version) == "1102":
                    ms.version = "1.10.2"

                embed=discord.Embed(title=" ", color=0x75df00)
                embed.set_author(name="genco.me Server Durumu", icon_url=mcIconURL)
                embed.add_field(name="Online :", value="✅Evet", inline=True)
                embed.add_field(name="Versiyon :", value=str(ms.version),inline= True)
                embed.add_field(name="Oyuncu Sayısı :", value=str(ms.current_players) + " / " + str(ms.max_players) ,inline= False)
                await client.send_message(message.channel,embed=embed)

            else:
                embed=discord.Embed(title=" ", color=0x75df00)
                embed.set_author(name="genco.me Server Durumu", icon_url=mcIconURL)
                embed.add_field(name="Online :", value="❌Hayır", inline=True)
                await client.send_message(message.channel,embed=embed)
        
                
token = os.environ['BOT_TOKEN']
client.run(token)



