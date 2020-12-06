import discord
import psycopg2
import random
from config import config
from discord.ext import commands


class Status(commands.Cog):

    def __init__(self, client):
        self.client = client 

    @commands.Cog.listener()
    async def on_ready(self):
        print('Status.py is ready')
    
    @commands.command()
    async def status(self, ctx):
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
            cur.execute("select * from Player where discord_id = %s;", (ctx.message.author.id,))
            rows = cur.fetchall()
            print(rows)
            for r in rows:
                id = r[0]
                gold = r[1]
                adv = r[2]
                lvl = r[3]
                p_exp = r[4]
            statusEmbed = discord.Embed(
                colour = 1752220
            )
            in_adv = "Currently in dungeon"
            if adv is None:
                in_adv = "Not in dungeon"
            statusEmbed.add_field(name="Status", value=f"Name: {ctx.message.author.name}\nLevel: {lvl}\nExp: {p_exp}\nGold: {gold}\nDungeon Status: {in_adv}")
            print(ctx.message.author.avatar_url)
            statusEmbed.set_thumbnail(url=f"{ctx.message.author.avatar_url}")
            await ctx.send(embed=statusEmbed)
        else:
            await ctx.send("Sir you haven't !isekai yet")
        cur.close()
        conn.close()


def setup(client):
    client.add_cog(Status(client))