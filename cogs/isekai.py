import discord
import psycopg2
import random
from config import config
from discord.ext import commands


class Isekai(commands.Cog):

    def __init__(self, client):
        self.client = client 

    @commands.Cog.listener()
    async def on_ready(self):
        print('Isekai.py is ready')
    @commands.command()
    async def questinfo(self, ctx, args = None):
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
                await ctx.send("You need to add the quest number first")
            else:

                if int(args) >= 1 and int(args) <= 99:
                    cur.execute("select boss_id, boss, hp, boss_race, exp_drop, lvl_req, descr from Boss where boss_id = %s", (args,))
                    rows = cur.fetchone()
                    boss_id = rows[0]
                    boss = rows[1]
                    hp = rows[2]
                    boss_race = rows[3]
                    exp_drop = rows[4]
                    lvl_req = rows[5]
                    descr = rows[6]
                    embed = discord.Embed(color=discord.Color.dark_green())
                    embed.add_field(name=f"Info on {boss}", value=f"**Boss Name:** {boss} **Boss HP:** {hp} \n**Boss Race:** {boss_race} \n\n **Description:** \n {descr}\n **Level Requirement:** {lvl_req}")
                    await ctx.message.channel.send(embed=embed)
                else:
                    await ctx.send("You need to add a valid number")
        else:
            await ctx.send("Sir you haven't !isekai yet")
        cur.close()
        conn.commit()
        conn.close()        
    @commands.command()
    async def quest(self, ctx):
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
            cur.execute("select lvl from Player where discord_id = %s;", (ctx.message.author.id,))
            rows = cur.fetchone()
            cur.execute("select boss, boss_id, lvl_req from Boss where lvl_req <= %s;", (rows[0],))
            rows = cur.fetchall()
            quests = ""
            for r in rows:
                quests += f"{r[1]}" + ". " + r[0] + "\n"
            embed = discord.Embed(color=discord.Color.dark_green())
            embed.add_field(name="Questboard", value=quests)
            await ctx.message.channel.send(embed=embed)
        else:
            await ctx.send("Sir you haven't !isekai yet")
        cur.close()
        conn.commit()
        conn.close() 
    @commands.command()
    async def isekai(self, ctx):
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("select discord_id from Player;")
        rows = cur.fetchall()
        player_exist = False
        for r in rows:            
            if r[0] == ctx.message.author.id:
                player_exist = True
                break
        if player_exist == True:
            await ctx.send('Your adventure has already started')
        else:
            death_messages = ["You died of a heartattack after trying to \
                save a girl from a tractor that was never going to hit her",
                "You died after getting a visit from Truck-kun",
                "You have been killed by Ali's giant ham",
                "You are being summoned to a different world to save it from a crisis!",
                "You lived a fulfilling life and died of old age. As a reward you get a chance at a second life",
                "You have died due to overwork from a black company",
                "You have died as a NEET otaku"]
                
            isekaiEmbed = discord.Embed(
                colour = 1752220
            )
            isekaiEmbed.add_field(name = "Welcome to the Afterlife!", value=f"{random.choice(death_messages)}\
                \n\nYou will now be reincarnated into a fantasy world with Swords and Magic! \
                \nHowever you will not get a cheat ability so do your best to survive!")            
            cur.execute("insert into player (discord_id, p_money, lvl, p_exp) values (%s, %s, %s, %s);", ((ctx.message.author.id,), 0, 1, 0))
            await ctx.send(embed=isekaiEmbed)
        cur.close()
        conn.commit()
        conn.close()


def setup(client):
    client.add_cog(Isekai(client))