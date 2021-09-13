import discord
import os
import psycopg2
from config import config
from discord.ext import commands

client = commands.Bot(command_prefix = '!')

client.remove_command('help')
@client.event
async def on_ready():
    print(f'Bot is online')
    params = config()
    conn = psycopg2.connect(**params)
    cur = conn.cursor()
    cur.execute("select rarity from Gacha where rarity_id is NULL;")
    rows = cur.fetchall()
    for r in rows:
        if r[0] == "N":
            cur.execute("update Gacha set rarity_id = %s where rarity = 'N';", (784587962037829662,))
        elif r[0] == "R":
            cur.execute("update Gacha set rarity_id = %s where rarity = 'R';", (784587951479848994,))
        elif r[0] == "SR":
            cur.execute("update Gacha set rarity_id = %s where rarity = 'SR';", (784587938846867493,))
        elif r[0] == "SSR":
            cur.execute("update Gacha set rarity_id = %s where rarity = 'SSR';", (784587928667029554,))
        elif r[0] == "UR":
            cur.execute("update Gacha set rarity_id = %s where rarity = 'UR';", (784587909495128066,))
    cur.close()
    conn.commit()
    conn.close()

@client.command()
async def update_rarity(ctx):
    if ctx.message.author.id == 135151849320873986:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("select rarity from Gacha where rarity_id is NULL;")
        rows = cur.fetchall()
        for r in rows:
            if r[0] == "N":
                cur.execute("update Gacha set rarity_id = %s where rarity = 'N';", (784587962037829662,))
            elif r[0] == "R":
                cur.execute("update Gacha set rarity_id = %s where rarity = 'R';", (784587951479848994,))
            elif r[0] == "SR":
                cur.execute("update Gacha set rarity_id = %s where rarity = 'SR';", (784587938846867493,))
            elif r[0] == "SSR":
                cur.execute("update Gacha set rarity_id = %s where rarity = 'SSR';", (784587928667029554,))
            elif r[0] == "UR":
                cur.execute("update Gacha set rarity_id = %s where rarity = 'UR';", (784587909495128066,))
        cur.close()
        conn.commit()
        conn.close()         
@client.command()
async def help(ctx):
    embed = discord.Embed(color=discord.Colour.red())
    embed.add_field(name="Everything you need to know\n", value="**!isekai** - You need to isekai because I need your soul if you wanna use my gacha\n**!h1** - Do a single pull\n**!h10** - Do a multi \
        \n**!gdb** <char name> - Search the database for characters\n**!cbox** - Check your character box\n**!sugoinfo** - Current information about the gacha\n\nEvery other command is WIP")
    await ctx.message.channel.send(embed=embed)   

@client.command()
async def load(ctx, extension):
    if ctx.message.author.id == 135151849320873986:
        client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    if ctx.message.author.id == 135151849320873986:
        client.unload_extension(f'cogs.{extension}')

@client.command()
async def reload(ctx, extension):
    if ctx.message.author.id == 135151849320873986: 
        client.unload_extension(f'cogs.{extension}')
        client.load_extension(f'cogs.{extension}')

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









f = open("token.txt", "r")
client.run(f.readline())