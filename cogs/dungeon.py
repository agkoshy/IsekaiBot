import discord
import datetime
import psycopg2
from config import config
from datetime import timedelta
from datetime import date
from discord.ext import commands



class Dungeon(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Dungeon is ready ")
    
    @commands.command()
    async def dungeon(self, ctx):
        params = config()
        conn = psycopg2.connect(**params)
        x = datetime.datetime.now() + timedelta(seconds=10)
        y = x.strftime('%Y-%m-%d %H:%M:%S')
        print(y)
        cur = conn.cursor()
        cur.execute("select count(*) from Player where discord_id = %s;", (ctx.message.author.id,))
        rows = cur.fetchall()
        player_exist = True
        for r in rows:
            if r[0] == 0:
                player_exist = False
        if player_exist == True:
            cur.execute("select adv from Player where discord_id = %s;", (ctx.message.author.id,))
            rows = cur.fetchall()
            adv = 0
            for r in rows:
                print(r[0])
                if r[0] is None:
                    cur.execute("update Player set adv = %s where adv is NULL and discord_id = %s", (y, ctx.message.author.id))
                    adv = y
                    break
                else:
                    adv = r[0]
            z = datetime.datetime.now()
            now = z.strftime('%Y-%m-%d %H:%M:%S')
            print("Before strptime %s", adv)
            if type(adv) == str:            
                adv = datetime.datetime.strptime(adv, '%Y-%m-%d %H:%M:%S')       
            now = datetime.datetime.strptime(now, '%Y-%m-%d %H:%M:%S')
            if (now > adv):
                #Makes their adventure status as NULL            
                cur.execute("update Player set adv = NULL where discord_id = %s", (ctx.message.author.id,))
                cur.execute("select p_exp, lvl from Player where discord_id = %s;", (ctx.message.author.id,))
                rows = cur.fetchall()
                for r in rows:
                    exp = r[0]
                    lvl = r[1]
                exp = exp + 30
                cur.execute("update Player set p_exp = %s where discord_id = %s", (exp, ctx.message.author.id))
                cur.execute("select ex from Lvl where lvl = %s;", (lvl,))
                rows = cur.fetchall()
                for r in rows:
                    exp_req = r[0]
                if exp < exp_req:
                    await ctx.send("You have completed the dungeon! You gained 30 exp!")
                else:
                    cur.execute("update Player set lvl = %s where discord_id = %s", (lvl + 1, ctx.message.author.id))
                    await ctx.send("You have completed the dungeon! You gained 30 exp! You have leveled up!")
            else:
                duration = adv - now 
                print(adv)
                print(now)
                print(duration)
                await ctx.send(f"You have {duration} remaining to complete the dungeon")
        else:
            await ctx.send("Sir you haven't !isekai yet")
        cur.close()
        conn.commit()
        conn.close()   

        # if (datetime.datetime.now() > x) :
        #     await ctx.send("test1")
        # else:
        #     print(x)
            
        #     print(datetime.datetime.now())
        #     await ctx.send(ctx.message.author.id)

def setup(client):
    client.add_cog(Dungeon(client))