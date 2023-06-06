import discord
from discord.ext import commands, tasks
import asyncio
import random
import os
import time
import re
from discord import SlashCommand
from discord.ext.commands import Bot

intents = discord.Intents.all()
intents.guilds = True

#config = { 'token': 'your-token', 'prefix': '?',}

#client = commands.Bot(command_prefix=config['prefix'], intents=intents)
client = commands.Bot(command_prefix=".", intents=intents)
bot = discord.Bot()
# slash = SlashCommand(client, sync_commands=True, description = 'yes')
@client.command()
@commands.cooldown(1,3,commands.BucketType.user)
async def test(ctx):
    await ctx.send("woofa")

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
    
@bot.command(description="What version have bot right now.")
async def version(ctx):
    await ctx.respond('a0.3.2')

@client.command(description = "Ping", guild=discord.Object(id=714247661515046975))
async def pingg(message):
    await message.send(f"Pong! {message.author.mention}")

@bot.command(description = "Brekfast") #Команда
async def breakfast(ctx):
    #random.seed(int(time.localtime()))
    choosenq=None #В конце нужно 
    choosenbf=None
    breakfasts=["Doge","Taxist", "Taxi", "Bread","Dragon","Pee","Poop","Tractorman","Egg", "Pepepopo", "Windmill", "Half Dead Poop", "Fridge", "Jesus", "Cat", "Revived Himself/Herself", "Clown", "Door", "suberdabber", "Gravestone", "Coconut", "Duck", "TheBrain", "Miguel", "Demon", "Frozen Salami", "Salami", "Carrot", "Furnace", "Dove", "Table", "Metal", "Farts", "Spike", "Oil Drill", "MrVolkov", "zheka01", "F1nch"] #Еда
    quality=["Fried","Woofable","Fat","Cooked","Aten","Pooped","Ugly","Beautiful","Weird","Acid","Powerful", "Badly", "Salted", "Rude", "Himself/Herself", "Yummy", "Broken", "Scaring", "Cold", "Doged", "Cute", "Blue Screen`d", "Vomitable", "Dead", "Small", "Big", "Maniacal", "Massaged", "Yucky", "Melted", "Annoying:skull:", "Godly", "Charming", "Abandoned", "Plastic", "Smelly", "Cool"] #Качество
    woofakbf=random.randint(1,len(breakfasts))-1 #Рандомно выбираем
    woofakq=random.randint(1,len(quality))-1 #Рандомно выбираем
    choosenbf=breakfasts[woofakbf]
    choosenq=quality[woofakq]
    await ctx.respond(f"{ctx.author.mention} will eat {choosenq} {choosenbf} for breakfast!") #Для примера @TheBrain will eat Fried Dragon

@bot.command(description = "Craft armor") #Команда
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
    # await message.respond(f"{message.author.mention} will craft
    #                         [chosenq] [chosena]
    #                         [chosenpr]
    #                         [chosendu]
    #                         [chosenth]") 

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

bot.run(token)
client.run(token)
