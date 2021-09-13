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
    async def geardb(self, ctx):
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
            a=3
        # for r in rows:
        #     gear_id = r[0]
        #     cur.execute("insert into Player_Gear (discord_id) values (%s);", (r[0],))
        #     cur.execute("insert into Player_Inventory (discord_id) values (%s);", (r[0],))
        # cur.execute("select discord_id from Player;")
        # rows = cur.fetchall()        
        # for r in rows:
        #     cur.execute("insert into Player_Stats (discord_id, str, intl, dex, vit, agi, wis, crit, acc) values (%s, 1, 1, 1, 1, 1, 1, 5, 70)", (r[0],))
            
        cur.close()
        conn.commit()
        conn.close() 
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
            cur.execute("select helm, chest, pants, boots, gloves, necklace, ring, cape, weapon, offhand_weapon from Player_Gear where discord_id = %s;", (ctx.message.author.id,))
            r = cur.fetchone()
            helm = r[0]
            chest = r[1]
            pants = r[2]
            boots = r[3]
            gloves = r[4]
            necklace = r[5]
            ring = r[6]
            cape = r[7]
            weapon = r[8]
            offhand = r[9]
            embed = discord.Embed(color=discord.Color.orange())
            embed.add_field(name="Equipped Gear", value=f"Helmet: {helm}\nChestpiece: {chest}\nGloves: {gloves}\nPants: {pants}\nBoots: {boots}\n")
            embed.add_field(name="** **", value=f"Cape: {cape}\nNecklace: {necklace}\nRing: {ring}", inline=False)
            #embed.add_field(name="** **", value="** **", inline=False)
            embed.add_field(name="** **", value=f"Weapon: {weapon}\n Weapon 2: {offhand}")
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
                await ctx.send("Need to specify the equipment you want to add")
            else:
                sql = """select count(*) from (select lower(gear) as gear from Gear) as G where gear like %s;"""
                search = f'%{args}%'
                cur.execute(sql, (search,))
                print(cur.mogrify(sql, (search,)))
                rows = cur.fetchone()
                if rows[0] == 0:
                    print("Doesn't exist")
                elif rows[0] == 1:
                    print("1 exists")
                    sql = """select gear, equiptype, gear_id from (select lower(gear) as gear, equiptype, gear_id from Gear) as G where gear like %s;"""
                    search = f'%{args}%'
                    cur.execute(sql, (search,))
                    print(cur.mogrify(sql, (search,)))
                    rows = cur.fetchone()
                    cur.execute("select gear from Gear where gear_id = %s;", (rows[2],))
                    r = cur.fetchone()
                    if rows[1] == "Sword":
                        cur.execute("update Player_Gear set weapon = %s where discord_id = %s;", (r[0], ctx.message.author.id))
                else:
                    print("more than 1")
        else:
            ctx.send("You haven't !isekai yet sir")
        cur.close()
        conn.commit()
        conn.close() 

def setup(client):
    client.add_cog(Equip(client))