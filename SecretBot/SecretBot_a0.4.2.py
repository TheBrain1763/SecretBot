import discord
from discord.ext import commands, tasks
import asyncio
from random import randint
import os
import datetime, time
import re
from discord import SlashCommand
from discord.ext.commands import Bot
import sys

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
start_time = time.time()
AUTHORIZED_USER_ID = 563034812676571176

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
    await ctx.respond('a0.4.2')

@client.command(description = "Ping", guild=discord.Object(id=714247661515046975))
async def pingg(message):
    await message.send(f"Pong! {message.author.mention}")
    
@client.command()
async def uptime(ctx):
    uptime = time.time() - start_time
    hours, remainder = divmod(int(uptime), 3600)
    minutes, seconds = divmod(remainder, 60)
    days, hours = divmod(hours, 24)
    await ctx.send(f"Бот работает: {days} дней, {hours} часов, {minutes} минут, {seconds} секунд")
    
@client.command()
async def restart(message):
    if message.author.id != AUTHORIZED_USER_ID:
        await message.send("You dont have access to that command.")
        return
    
    await message.send("Restarting...")
    os.execv(sys.executable, ['python'] + sys.argv)

# @client.event
# async def on_ready():
#     print('Logged in as {0} ({0.id})'.format(bot.user))

@bot.command(description = "Brekfast") #Команда
async def breakfast(ctx):
    #random.seed(int(time.localtime()))
    choosenq=None #В конце нужно 
    choosenbf=None
    choosentr = None
    breakfasts=["Doge","Taxist", "Taxi", "Bread","Dragon","Pee","Poop","Tractorman","Egg", "Pepepopo", "Windmill", "Half Dead Poop", "Fridge", "Jesus", "Cat", "Revived Himself/Herself", "Clown", "Door", "suberdabber", "Gravestone", "Coconut", "Duck", "TheBrain", "Miguel", "Demon", "Frozen Salami", "Salami", "Carrot", "Furnace", "Dove", "Table", "Metal", "Farts", "Spike", "Oil Drill", "MrVolkov", "zheka01", "F1nch"] #Еда
    quality=["Fried","Woofable","Fat","Cooked","Aten","Pooped","Ugly","Beautiful","Weird","Acid","Powerful", "Badly", "Salted", "Rude", "Himself/Herself", "Broken", "Scaring", "Cold", "Doged", "Cute", "Blue Screen`d", "Vomitable", "Dead", "Small", "Big", "Maniacal", "Massaged", "Yucky", "Melted", "Godly", "Charming", "Abandoned", "Plastic", "Smelly", "Cool", "Angry", "Sussy"] #Качество
    woofakbf=randint(1,len(breakfasts))-1 #Рандомно выбираем
    woofakq=randint(1,len(quality))-1 #Рандомно выбираем
    choosenbf=breakfasts[woofakbf]
    choosenq=quality[woofakq]
    if randint(1,275) == 1:
        choosenq = 'Annoying:skull:'
    if randint(1,300) == 1:
        choosentr = 'Get Trolled'
        
    await ctx.respond(f"{ctx.author.mention} will eat {choosenq} {choosenbf} for breakfast!\n {[choosentr]}") #Для примера @TheBrain will eat Fried Dragon

@bot.command(description = "Craft armor!")
async def armor(message):
    #random.seed(int(time.localtime()))
    chosenq = None
    chosena = None
    chosenpr = None
    chosendu = None
    chosenth = None
    chosencr = None
    chosende = None
    chosenev = None
    #armor = ["Wooden", "Stone", "Iron", "Diamond", "Emerald", "Fognium", "Ruby", "???", "Egg warrior", "Spiked", "AIR?!?!"] #Броня
    # quality = [":white_circle:", ":green_circle:", ":blue_circle:", ":purple_circle:", ":yellow_cirle:", ":red_circle:", "GL9I51T=9S3H5E6D"] #Качество
    # protection = ["I", "II", "III", "IV", "V", "VI", "VII", "IX", "X"] #Защита
    # durability = ["I", "II", "III", "IV", "V", "VI", "VII", "IX", "X"] #Прочность
    # thorns = ["I", "II", "III", "IV", "V", "VI", "VII", "IX", "X"] #Шипы
    if randint(1,639) == 1:
        chosencr = '**Cracked 1/639**'
    if randint(1,55) == 1:
        chosenev = '**Evolved 1/55**'
    
    if randint(1,29) == 1:
        chosende = 'Decorated with Wooden 1/29'
    if randint(1,58) == 1:
        chosende = 'Decorated with Stone 1/58'
    if randint(1,355) == 1:
        chosende = 'Decorated with Iron 1/355'
    if randint(1,1005) == 1:
        chosende = 'Decorated with Diamonds 1/1005'
    if randint(1,2555) == 1:
        chosende = 'Decorated with Emeralds 1/2555'
    if randint(1,5555) == 1:
        chosende = 'Decorated with Fogniums 1/5555'
    if randint(1,10258) == 1:
        chosende = '**Decorated with Rubyes 1/10258**'
    if randint(1,50100) == 1:
        chosende = '**Decorated with Spikes 1/50100**'
    if randint(1,150000) == 1:
        chosende = '**Decorated with... AIR?!?!? 1/150000**'
      
    if randint(1,1) == 1:
        chosena = 'Wooden Armor 1/1'
    if randint(1,3) == 1:
        chosena = 'Stone Armor 1/3'
    if randint(1,8) == 1:
        chosena = 'Iron Armor 1/8'
    if randint(1,35) == 1:
        chosena = 'Diamond Armor 1/35'
    if randint(1,110) == 1:
        chosena = 'Emerald Armor 1/110'
    if randint(1,569) == 1:
        chosena= 'Fognium Armor 1/569'
    if randint(1,1300) == 1:
        chosena = 'Ruby Armor 1/1300'
    if randint(1,2099) == 1:
        chosena = 'Egg Warrior Armor 1/2099'
    if randint(1,5500) == 1:
        chosena= 'Spiked Armor 1/5500'
    if randint(1,10500) == 1:
        chosena = '**...AIR ARMOR?!?!? 1/10500**'
    if randint(1,1000000) == 1:
        chosena = '**By mistake you crafted sword(What?)**'
    
    if randint(1,1) == 1:
        chosenq = ':white_circle:'
    if randint(1,15) == 1:
        chosenq = ':green_circle:'
    if randint(1,45) == 1:
        chosenq = ':blue_circle:'
    if randint(1,105) == 1:
        chosenq= ':purple_circle:'
    if randint(1,250) == 1:
        chosenq = ':yellow_cirle:'
    if randint(1,1000) == 1:
        chosenq= ':red_circle:'
    if randint(1,2500) == 1:
        chosenq = '**GL9I51T=9S3H5E6D**'
    
    if randint(1,8) == 1:
        chosenpr = 'Protection: I'
    if randint(1,15) == 1:
        chosenpr = 'Protection: II'
    if randint(1,22) == 1:
        chosenpr = 'Protection: III'
    if randint(1,35) == 1:
        chosenpr = 'Protection: IV'
    if randint(1,49) == 1:
        chosenpr = 'Protection: V'
    if randint(1,169) == 1:
        chosenpr = 'Protection: VI'
    if randint(1,256) == 1:
        chosenpr = 'Protection: VII'
    if randint(1,506) == 1:
        chosenpr = 'Protection: IX'
    if randint(1,1005) == 1:
        chosenpr = 'Protection: X'
        
    if randint(1,8) == 1:
        chosendu = 'Durability: I'
    if randint(1,15) == 1:
        chosendu = 'Durability: II'
    if randint(1,22) == 1:
        chosendu = 'Durability: III'
    if randint(1,43) == 1:
        chosendu = 'Durability: IV'
    if randint(1,49) == 1:
        chosendu = 'Durability: V'
    if randint(1,169) == 1:
        chosendu = 'Durability: VI'
    if randint(1,256) == 1:
        chosendu = 'Durability: VII'
    if randint(1,506) == 1:
        chosendu = 'Durability: IX'
    if randint(1,1005) == 1:
        chosendu = 'Durability: X'
        
    if randint(1,8) == 1:
        chosenth = 'Thorns: I'
    if randint(1,15) == 1:
        chosenth = 'Thorns: II'
    if randint(1,22) == 1:
        chosenth= 'Thorns: III'
    if randint(1,43) == 1:
        chosenth = 'Thorns: IV'
    if randint(1,49) == 1:
        chosenth = 'Thorns: V'
    if randint(1,169) == 1:
        chosenth= 'Thorns: VI'
    if randint(1,256) == 1:
        chosenth = 'Thorns: VII'
    if randint(1,506) == 1:
        chosenth = 'Thorns: IX'
    if randint(1,1005) == 1:
        chosenth = 'Thorns: X'
        
    await message.respond(f"{message.author.mention} You will craft...\n{[chosenq]} {[chosena]}\n{[chosende]}\n{[chosencr]}\n{[chosenev]}\n{[chosenpr]}\n{[chosendu]}\n{[chosenth]}")
    
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

# async def start():
#     await asyncio.gather(bot.start(token), client.start(token))
# loop = asyncio.get_event_loop()
# loop.run_until_complete(start())
async def run_client():
    await client.start(token)

async def run_bot():
   await bot.start(token)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.gather(run_client(), run_bot()))
