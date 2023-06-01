import discord
from discord.ext import commands, tasks
import asyncio
import random
import os
import time
import re
from discord_slash import SlashCommand

intents = discord.Intents.default()
intents.guilds = True

#config = { 'token': 'your-token', 'prefix': '?',}

#client = commands.Bot(command_prefix=config['prefix'], intents=intents)
client = commands.Bot(command_prefix='/', intents=intents, application_id = 1111923270506270730)
#bot = discord.Bot(intents=intents)
slash = SlashCommand(client, sync_commands=True)

token =' '

# @client.event
# async def on_message(message):
#     await message.reply(message.content)

# @client.command(pass_context=True)
# async def say(ctx):
#     msg = ctx.message.content.split(" ", 1)
#     await client.delete_message(ctx.message)
#     await client.send_message(ctx.message.channel, msg)
        
# @client.event
# async def on_message(message):
#     if message.author != client.user:
#         await message.reply(message.content)

hi_RU = ["Привет!", "Ку", "Здарова!", "Хаюхай!", "Хей бро!", "Хей!", "Ну и пока", "Хеллоу!", "Здравствуй!", "Здравствуйте!", "Привет, Санек!"]
hi_ENG = ["Hi", "Hello", "Wassup", "You are welcome!", "Welcome"]
    
@client.slash(name = "version", description = "test")
async def version(message):
    await message.send('a0.3.0')
    
@client.slash(description="Testa")
async def testa(ctx):
    ctx.respond("This is a test!")

@client.command()
async def pingg(message):
    await message.send(f"Pong! {message.author.mention}")

@client.slash(name = "breakfast", description = "test")
async def breakfast(ctx):
    #random.seed(int(time.localtime()))
    choosenq=None
    choosenbf=None
    breakfasts=["Doge","Taxist","Bread","Dragon","Pee","Poop","Tractorman","Egg", "Pepepopo"]
    quality=["Fried","Woofable","Fat","Cooked","Aten","Pooped","Ugly","Beautiful","Weird","Acid","Powerful"]
    woofakbf=random.randint(1,len(breakfasts))-1
    woofakq=random.randint(1,len(quality))-1
    choosenbf=breakfasts[woofakbf]
    choosenq=quality[woofakq]
    await ctx.reply(f"{ctx.author.mention} will eat {choosenq} {choosenbf}")

@client.slash(name = "armor", description = "test")
async def armor(message):
    #random.seed(int(time.localtime()))
    chosenq = None
    chosena = None
    chosenpr = None
    chosendu = None
    chosenth = None
    armor = ["Wooden", "Stone", "Iron", "Diamond", "Emerald", "Fognium", "Ruby", "???", "Egg warrior", "Spiked", ]
    quality = [":white_circle:", ":green_circle:", ":blue_circle:", ":purple_circle:", ":yellow_cirle:", ":red_circle:", "GL9I51T=9S3H5E6D"]
    protection = ["I", "II", "III", "IV", "V", "VI", "VII", "IX", "X"]
    durability = ["I", "II", "III", "IV", "V", "VI", "VII", "IX", "X"]
    thorns = ["I", "II", "III", "IV", "V", "VI", "VII", "IX", "X"]
    woofkaq=random.randint(1,len(quality))-1
    woofkaa=random.randint(1,len(armor))-1
    woofkapr=random.randint(1,len(protection))-1
    woofkadu=random.randint(1,len(durability))-1
    woofkath=random.randint(1,len(thorns))-1
    chosenq = quality[woofkaq]
    chosena = armor[woofkaa]
    chosenpr = protection[woofkapr]
    chosendu = durability[woofkadu]
    chosenth = thorns[woofkath]
    await message.reply(f"{message.author.mention} will craft"
                   [chosenq] [chosena]
                   [chosenpr]
                   [chosendu]
                   [chosenth])

# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return
#     if message.content == 'Привет':
#         greeting = random.choice(hi_RU)
#         await message.channel.send(greeting)
#     elif message.content == 'Ку':
#         greeting = random.choice(hi_RU)
#         await message.channel.send(greeting)
#     elif message.content == 'Хеллоу':
#         greeting = random.choice(hi_RU)
#         await message.channel.send(greeting)
#     elif message.content == 'Хей':
#         greeting = random.choice(hi_RU)
#         await message.channel.send(greeting)
#     elif message.content == 'Хаюхай':
#         greeting = random.choice(hi_RU)
#         await message.channel.send(greeting)
#     elif message.content == 'Хей бро':
#         greeting = random.choice(hi_RU)
#         await message.channel.send(greeting)
#     elif message.content == 'Здравствуй':
#         greeting = random.choice(hi_RU)
#         await message.channel.send(greeting)
#     elif message.content == 'Здравствуйте':
#         greeting = random.choice(hi_RU)
#         await message.channel.send(greeting)
#     elif message.content == 'Доброе утро':
#         greeting = random.choice(hi_RU)
#         await message.channel.send(greeting)
#     elif message.content == 'Добрый вечер':
#         greeting = random.choice(hi_RU)
#         await message.channel.send(greeting)
#     elif message.content == 'Доброй ночи':
#         greeting = random.choice(hi_RU)
#         await message.channel.send(greeting)
#     elif message.content == 'Здравия желаю':
#         greeting = random.choice(hi_RU)
#         await message.channel.send(greeting)
#     elif message.content == 'Wassup':
#         greeting = random.choice(hi_ENG)
#         await message.channel.send(greeting)
#     elif message.content == 'Hi':
#         greeting = random.choice(hi_ENG)
#         await message.channel.send(greeting)
#     elif message.content == 'Hello':
#         greeting = random.choice(hi_ENG)
#         await message.channel.send(greeting)
#     elif message.content == 'Good evening':
#         greeting = random.choice(hi_ENG)
#         await message.channel.send(greeting)
#     elif message.content == 'Good morning':
#         greeting = random.choice(hi_ENG)
#         await message.channel.send(greeting)
#     elif message.content == 'Morning':
#         greeting = random.choice(hi_ENG)
#         await message.channel.send(greeting)

client.run(token)