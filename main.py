from discord.ext import commands
import discord
import time
import random
import os
botToken = str(os.getenv('PARROT_BOT_TOKEN'))
print(botToken)
channelID = 999431862399287409
lastChannel = None
wordsSaid:list = ["squawk","hahaha"]
bannedWords = ["p>","p!"]
birdNoises = ["sqwuak","ha hahe","twee-tweet","lalalaa"]
birdActivities = ["\*fucking divebombs you\*", "\*hiss\*", "\*shits\*"]
bot = commands.Bot(command_prefix="p>",intents=discord.Intents.all()) #    look a bear  8( :(0<)

def addToWordsSaid(text:str):
    global wordsSaid
    text = text.split(" ")
    wordsSaid = wordsSaid + text
    wordsSaid = [i for i in wordsSaid if not i.lower() in bannedWords]

def getRandomWords():
    text = random.choice(birdNoises)
    randomWords = random.sample(wordsSaid,2)
    text += (" " + randomWords[0])
    text += (" " + randomWords[1])
    return text

@bot.event
async def on_ready():
    print("parrot is readey")
    channel = bot.get_channel(channelID)
    lastChannel = channel
    await channel.send("haha")

@bot.event
async def on_message(message):
    global wordsSaid
    if message.author == bot.user:
        return
    elif random.randint(1,20)==1 or message.content[:2] == "p!":
        await message.channel.send( random.choice(birdActivities) )
        return
    addToWordsSaid(message.content)
    if random.randint(1,5) == 1 or message.content[:2] == "p>":
        await message.channel.send(getRandomWords())

bot.run(botToken)