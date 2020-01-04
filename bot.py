import discord
from discord.ext import commands

client = discord.Client()

@client.event
async def on_ready():
    print('Bot is ready and is logged on as {0.user}'.format(client))

client.run('NjYxMzM1MDQ5Mjk1MjMzMDI1.Xg14Mg.AfuhUP9bPfQJc54p8e6AQF8os28')
