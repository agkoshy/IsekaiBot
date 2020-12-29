import discord
import psycopg2
import random
from config import config
from discord.ext import commands


class Equip(commands.Cog):

    def __init__(self, client):
        self.client = client 

    @commands.Cog.listener()
    async def on_ready(self):
        print('Equip.py is ready')

    @commands.command()
    async def gear(self, ctx):
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("select count(*) from Player where discord_id = %s;", (ctx.message.author.id,))
        rows = cur.fetchall()
        player_exist = True
        for r in rows:
            if r[0] == 0:
                player_exist = False
        if player_exist == True:
            embed = discord.Embed(color=discord.Color.orange())
            embed.add_field(name="Equipped Gear", value=f"Helmet: Goblin Slayer Helmet\nChestpiece: \nGloves: \nPants: \nBoots: \n")
            embed.add_field(name="** **", value=f"Cape: \nNecklace: \nRing: Hehe ring", inline=False)
            #embed.add_field(name="** **", value="** **", inline=False)
            embed.add_field(name="** **", value=f"Weapon: Ali's Ham\n Weapon 2: Ali's Ham")
            await ctx.message.channel.send(embed=embed)
        else:
            ctx.send("You haven't !isekai yet sir")
        cur.close()
        conn.commit()
        conn.close() 
    @commands.command()
    async def equip(self, ctx, args = None):
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("select count(*) from Player where discord_id = %s;", (ctx.message.author.id,))
        rows = cur.fetchall()
        player_exist = True
        for r in rows:
            if r[0] == 0:
                player_exist = False
        if player_exist == True:
            if args is None:
                ctx.send("Need to specify the equipment you want to add")
        else:
            ctx.send("You haven't !isekai yet sir")
        cur.close()
        conn.commit()
        conn.close() 

def setup(client):
    client.add_cog(Equip(client))