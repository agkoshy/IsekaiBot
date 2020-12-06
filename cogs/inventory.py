import discord
import psycopg2
import random
import DiscordUtils
from config import config
from discord.ext import commands

class Inventory(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Inventory.py is ready')

    @commands.command()
    async def inventory(self, ctx):
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
            cur.execute("select gear from Gear limit 15;")
            rows = cur.fetchall()
            inv_list = ""
            for r in rows:
                inv_list = inv_list + r[0] + "\n"
            embed1 = discord.Embed(color=ctx.author.color).add_field(name="** **", value=f"{inv_list}")
            embed2 = discord.Embed(color=ctx.author.color).add_field(name="Example2", value="Page 2")
            embed3 = discord.Embed(color=ctx.author.color).add_field(name="Example3", value="Page 3")
            paginator = DiscordUtils.Pagination.AutoEmbedPaginator(ctx)
            embeds = [embed1, embed2, embed3]
            await paginator.run(embeds)
        else:
            await ctx.send("Sir you haven't !isekai yet")

        cur.close()
        conn.close()
    #     page1=discord.Embed(
    #         title='Page 1/3',
    #         description='Description',
    #         colour=discord.Colour.orange()
    #     )
    #     page2=discord.Embed(
    #         title='Page 2/3',
    #         description='Description',
    #         colour=discord.Colour.orange()
    #     )
    #     page3=discord.Embed(
    #         title='Page 3/3',
    #         description='Description',
    #         colour=discord.Colour.orange()
    #     )

    #     pages=[page1,page2,page3]

    #     message=await ctx.send(embed=page1)

    #     #await message.add_reaction('\u23ee')
    #     await message.add_reaction('\u25c0')
    #     await message.add_reaction('\u25b6')
    #    # await message.add_reaction('\u23ed')

    #     i=0
    #     emoji=''
        
    #     while True:
    #         if emoji=='\u23ee':
    #             i=0
    #             await message.edit(message,embed=pages[i])
    #         if emoji=='\u25c0':
    #             if i>0:
    #                 i-=1
    #                 await message.edit(message,embed=pages[i])
    #         if emoji=='\u25b6':
    #             if i<2:
    #                 i+=1
    #                 await message.edit(message,embed=pages[i])
    #         if emoji=='\u23ed':
    #             i=2
    #             await message.edit(message,embed=pages[i])

    #         res=await self.client.wait_for('message',timeout=30)
    #         if res==None:
    #             break
    #         if str(res[1])!='narbot#7284': #Example: 'MyBot#1111'
    #             emoji=str(res[0].emoji)
    #             await message.remove_reaction(message,res[0].emoji,res[1])

    #     await message.clear_reactions(message)

def setup(client):
    client.add_cog(Inventory(client))