import discord
from discord.ext import commands

client = commands.Bot(command_prefix = ':')

@client.event
async def on_ready():
    print('Bot has come alive.')

@client.event
async def on_member_join(member):
    print(f'{member} has joined the server.')

@client.event
async def on_member_remove(member):
    print(f'{member} has left a server.')

client.run('NzY4MDE2MDg4MDIwODExNzg2.X46UuA.j3Ip4z11NWwRJlShEXcfu6ii0pY')
