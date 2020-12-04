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