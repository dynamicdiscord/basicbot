import discord
from discord.ext import commands

client = discord.Client()

@client.event
async def on_ready():
    print('Bot is ready and is logged on as {0.user}'.format(client))

client.run('bot_token')
