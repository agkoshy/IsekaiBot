import discord
import os
import psycopg2
from config import config
from discord.ext import commands

client = commands.Bot(command_prefix = '!')
params = config()
conn = psycopg2.connect(**params)

# client.remove_command('help')
@client.event
async def on_ready():
    print(f'Bot is online')

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

# @client.event
# async def on_message(message):
    # cur = conn.cursor()
    # cur.execute("insert into player (discord_id, str, vit, intl, fth, luk, cha, wis, dex) values (%s, %s, %s, %s, %s, %s, %s, %s, %s);", ((message.author.id, ), 0, 0, 0, 0, 0, 0, 0, 0))
    # cur.execute("select discord_id from player where discord_id = %s", (message.author.id, ))
    # rows = cur.fetchall()

    # #for r in rows:
    #  #   if r[0] != message.author.id
           

    # cur.close()
    # conn.commit()
    # conn.close()

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')










client.run('NjA2ODgwMTc1NDY0MTIwMzI5.XURfNQ.CzTm9oGtDwCUAhUx2YwHJwycYc8')