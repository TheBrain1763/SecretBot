import discord
from discord.ext import commands
import asyncio
import random
import os
import time
import re

intents = discord.Intents.default()
intents.message_content = True

config = { 'token': 'your-token', 'prefix': '/',}

client = commands.Bot(command_prefix=config['prefix'], intents=intents)

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
    
@client.command()
async def version_command(message):
    await message.send('a0.2.2')
    
@client.command(name = "command_pingg")
async def pingg_command(ctx):
    await ctx.send(f"Pong! {ctx.author.mention}")

@client.command(name="command_breakfast")
async def breakfast_command(ctx):
    random.seed(int(time.localtime()))
    choosenq=None
    choosenbf=None
    breakfasts=["Doge","Taxist","Bread","Dragon","Pee","Poop","Tractorman","Egg", "Pepepopo"]
    quality=["Fried","Woofable","Fat","Cooked","Aten","Pooped","Ugly","Beautiful","Weird","Acid","Powerful"]
    woofakbf=random.randint(1,len(breakfasts))-1
    woofakq=random.randint(1,len(quality))-1
    choosenbf=breakfasts[woofakbf]
    choosenq=quality[woofakq]
    await ctx.send(f"{ctx.author.mention} will eat {choosenq} {choosenbf}")
@client.command(name="armor")
async def armor_command(ctx):
    random.seed(int(time.localtime()))
    choosenq = None
    choosena = None
    chosenpr = None
    chosendu = None
    chosenth = None
    armor = ["Wooden", "Stone", "Iron", "Diamond", "Emerald", "Fognium", "Ruby", "???", "Egg warrior", "Spiked", ]
    quality = [":white_circle:", ":green_circle:", ":blue_circle:", ":purple_circle:", ":yellow_cirle:", ":red_circle:", "GL9I51T=9S3H5E6D"]
    protection = ["I", "II", "III", "IV", "V", "VI", "VII", "IX", "X"]
    durability = ["I", "II", "III", "IV", "V", "VI", "VII", "IX", "X"]
    thorns = ["I", "II", "III", "IV", "V", "VI", "VII", "IX", "X"]
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == 'Привет':
        greeting = random.choice(hi_RU)
        await message.channel.send(greeting)
    if message.content == 'Ку':
        greeting = random.choice(hi_RU)
        await message.channel.send(greeting)
    elif message.content == 'Хеллоу':
        greeting = random.choice(hi_RU)
        await message.channel.send(greeting)
    elif message.content == 'Хей':
        greeting = random.choice(hi_RU)
        await message.channel.send(greeting)
    elif message.content == 'Хаюхай':
        greeting = random.choice(hi_RU)
        await message.channel.send(greeting)
    elif message.content == 'Хей бро':
        greeting = random.choice(hi_RU)
        await message.channel.send(greeting)
    elif message.content == 'Здравствуй':
        greeting = random.choice(hi_RU)
        await message.channel.send(greeting)
    elif message.content == 'Здравствуйте':
        greeting = random.choice(hi_RU)
        await message.channel.send(greeting)
    elif message.content == 'Доброе утро':
        greeting = random.choice(hi_RU)
        await message.channel.send(greeting)
    elif message.content == 'Добрый вечер':
        greeting = random.choice(hi_RU)
        await message.channel.send(greeting)
    elif message.content == 'Доброй ночи':
        greeting = random.choice(hi_RU)
        await message.channel.send(greeting)
    elif message.content == 'Здравия желаю':
        greeting = random.choice(hi_RU)
        await message.channel.send(greeting)
    elif message.content == 'Wassup':
        greeting = random.choice(hi_ENG)
        await message.channel.send(greeting)
    elif message.content == 'Hi':
        greeting = random.choice(hi_ENG)
        await message.channel.send(greeting)
    elif message.content == 'Hello':
        greeting = random.choice(hi_ENG)
        await message.channel.send(greeting)
    elif message.content == 'Good evening':
        greeting = random.choice(hi_ENG)
        await message.channel.send(greeting)
    elif message.content == 'Good morning':
        greeting = random.choice(hi_ENG)
        await message.channel.send(greeting)
    elif message.content == 'Morning':
        greeting = random.choice(hi_ENG)
        await message.channel.send(greeting)
        
client.run(token)
