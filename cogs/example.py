import discord
from discord.ext import commands

class Example(commands.Cog):

    def __init__(self, client):
        self.client = client 

    @commands.Cog.listener()
    async def on_ready(self):
        print('Example.py is ready')
    
    @commands.command()
    async def humza1(self, ctx):
        await ctx.send('Humza is haram')
        a = 32
        b = 15
        c = a/b
        print(int(c))


def setup(client):
    client.add_cog(Example(client))