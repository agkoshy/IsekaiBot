import discord
import psycopg2
from discord.ext import commands

class Postgres(commands.Cog):

 
    def __init__(self, client):
        self.client = client 
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('postgres is ready')


def setup(client):
    client.add_cog(Postgres(client))