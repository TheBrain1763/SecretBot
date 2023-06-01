import discord
from discord.ext import commands, tasks
import asyncio
import random
import os
import time
import re
from discord import Bot

intents = discord.Intents.default()
intents.guilds = True

#config = { 'token': 'your-token', 'prefix': '?',}

#client = commands.Bot(command_prefix=config['prefix'], intents=intents)
client = commands.Bot(command_prefix='/', intents=intents, application_id = 1111923270506270730,  sync_commands=True, description = 'yes')
bot = discord.Bot(intents=intents)
# slash = SlashCommand(client, sync_commands=True, description = 'yes')

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
    
@bot.slash_command(name = "version", description = "test")
async def version(message):
    await message.send('a0.3.0')

@bot.slash_command(name='azaza')
async def zeze(message):
    await message.send('Ololo')

    
@bot.slash_command(description="Testa")
async def testa(ctx):
    ctx.respond("This is a test!")

@bot.slash_command(name = "pingg", description = "Ping")
async def pingg(message):
    await message.send(f"Pong! {message.author.mention}")

@bot.slash_command(name = "breakfast", description = "test") #Команда
async def breakfast(ctx):
    #random.seed(int(time.localtime()))
    choosenq=None #В конце нужно 
    choosenbf=None
    breakfasts=["Doge","Taxist","Bread","Dragon","Pee","Poop","Tractorman","Egg", "Pepepopo"] #Еда
    quality=["Fried","Woofable","Fat","Cooked","Aten","Pooped","Ugly","Beautiful","Weird","Acid","Powerful"] #Качество
    woofakbf=random.randint(1,len(breakfasts))-1 #Рандомно выбираем
    woofakq=random.randint(1,len(quality))-1 #Рандомно выбираем
    choosenbf=breakfasts[woofakbf]
    choosenq=quality[woofakq]
    await ctx.reply(f"{ctx.author.mention} will eat {choosenq} {choosenbf}") #Для примера @TheBrain will eat Fried Dragon

@bot.slash_command(name = "armor", description = "test") #Команда
async def armor(message):
    #random.seed(int(time.localtime()))
    chosenq = None
    chosena = None
    chosenpr = None
    chosendu = None
    chosenth = None
    armor = ["Wooden", "Stone", "Iron", "Diamond", "Emerald", "Fognium", "Ruby", "???", "Egg warrior", "Spiked"] #Броня
    quality = [":white_circle:", ":green_circle:", ":blue_circle:", ":purple_circle:", ":yellow_cirle:", ":red_circle:", "GL9I51T=9S3H5E6D"] #Качество
    protection = ["I", "II", "III", "IV", "V", "VI", "VII", "IX", "X"] #Защита
    durability = ["I", "II", "III", "IV", "V", "VI", "VII", "IX", "X"] #Прочность
    thorns = ["I", "II", "III", "IV", "V", "VI", "VII", "IX", "X"] #Шипы
    woofkaq=random.randint(1,len(quality))-1 #Рандомно выбираем
    woofkaa=random.randint(1,len(armor))-1            #  I: 1/1
    #                                                     II: 1/6
    #                                                     III: 1/22
    #                                                     IV: 1/41
    #                                                     V: 1/47
    #                                                     VI: 1/57
    #                                                     VII: 1/107
    #                                                     VIII: 1/255
    #                                                     IX: 1/505
    #                                                     X: 1/1000
    woofkapr=random.randint(1,len(protection))-1
    woofkadu=random.randint(1,len(durability))-1
    woofkath=random.randint(1,len(thorns))-1
    chosenq = quality[woofkaq]
    chosena = armor[woofkaa]
    chosenpr = protection[woofkapr]
    chosendu = durability[woofkadu]
    chosenth = thorns[woofkath]
    await message.reply(f"{message.author.mention} will craft" #К примеру @TheBrain will craft...
                   [chosenq] [chosena]                         #            :кружок: Stone Sword 1/1
                   [chosenpr]                                  #            и зачары с маленьким шансом
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
