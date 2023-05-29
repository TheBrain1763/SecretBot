import discord
from discord.ext import commands
import asyncio
import random
import os
import time

intents = discord.Intents.default()
intents.message_content = True

config = { 'token': 'your-token', 'prefix': 'prefix',}

client = commands.Bot(command_prefix=config['prefix'], intents=intents)

token ='MTExMTkyMzI3MDUwNjI3MDczMA.GTvdRM.A11R7drhR0sJNCNpiwNObRYw70S3Fqy9s1v8S0'

# @client.event
# async def on_message(message):
#     await message.reply(message.content)

# @client.command(pass_context=True)
# async def say(ctx):
#     msg = ctx.message.content.split(" ", 1)
#     await client.delete_message(ctx.message)
#     await client.send_message(ctx.message.channel, msg)
        
@client.event
async def on_message(message):
    if message.author != client.user:
        await message.reply(message.content)
        
# @client.command()
# async def version(message):
#     await message.send('a0.0.1')

client.run(token)