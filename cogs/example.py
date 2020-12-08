import discord
import random
import datetime
from datetime import timedelta
from datetime import date
from discord.ext import commands

class Example(commands.Cog):

    def __init__(self, client):
        self.client = client 

    @commands.Cog.listener()
    async def on_ready(self):
        print('Example.py is ready')
    
    @commands.command()
    async def slack(self, ctx):
        dnow = datetime.datetime.now()
        d = datetime.datetime(dnow.year, dnow.month, dnow.day, 4, 00)
        now = datetime.datetime.now()
        x = d.strftime('%H:%M:%S')
        y = now.strftime('%H:%M:%S')
        now = datetime.datetime.strptime(y, '%H:%M:%S')
        d = datetime.datetime.strptime(x, '%H:%M:%S')
        print(now - d)
        if (now < d):
            await ctx.send("You haven't started work to slack on")
        else:
            rng = random.randint(1, 5)
            if rng == 1:
                await ctx.send(f"You have slacked for {now - d}")
            elif rng == 2:
                await ctx.send(f"You have beat meat for {now - d}")
            elif (rng == 3):
                await ctx.send(f"You have {now - d} of phone screentime")
            elif (rng == 4):
                await ctx.send(f"You have played fgo for {now - d}")
            elif (rng == 5):
                await ctx.send(f"You have browsed pixiv for {now - d}")
      
        # await ctx.send('Humza is haram')
        # a = 32
        # b = 15
        # c = a/b
        # print(int(c))
        


def setup(client):
    client.add_cog(Example(client))