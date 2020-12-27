import discord
import psycopg2
import random
import datetime
from datetime import timedelta
import DiscordUtils
import asyncio
from config import config
from discord.ext import commands

class Battle(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Battle.py is ready')
    
    # @commands.Cog.listener()
    # async def on_reaction_add(self, reaction, uesr):
    #     print("heh")
    @commands.command()
    async def battle(self, ctx, args = None):
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
            #Not in Dungeon, Still Exploring Dungeon, Ready, Ongoing, Finished
            cur.execute("select game_state from Player where discord_id = %s", (ctx.message.author.id,))
            row = cur.fetchone()
            if row[0] == "Not in Dungeon":
                await ctx.send("You are not in a dungeon yet")
            elif row[0] == "Still Exploring Dungeon":
                await ctx.send("You are still exploring the dungeon")
            elif row[0] == "Ready":
                #Chooses which attack to do
                if args is None:
                    x = datetime.datetime.now() + timedelta(seconds=60)
                    #while ()
                    embed = discord.Embed(color=discord.Color.dark_red())
                    boss_hp = 10
                    hp = 15
                    embed.add_field(name="Goblin HP:", value=boss_hp, inline=False)
                    embed.add_field(name="HP:", value=hp, inline=False)
                    embed.add_field(name="Attacks: ", value="Attack 1\nHeal\nAttack 2\nHehe")
                    embed.set_thumbnail(url="https://assets.stickpng.com/images/5b4eee54c051e602a568ce1b.png")
                    embed.set_footer(text=ctx.message.author.name, icon_url=ctx.message.author.avatar_url)
                    #msg = ctx.message.channel.send(embed=embed)
                    
                    msg = await ctx.message.channel.send(embed=embed)
                    # await msg.add_reaction(self.client.get_emoji(788500845233700905))
                    # await msg.add_reaction(self.client.get_emoji(788500845183631391))
                    # await msg.add_reaction(self.client.get_emoji(788500845385482300))
                    # await msg.add_reaction(self.client.get_emoji(788500845414580256))
                elif args == "1":
                    await ctx.send("<:gotojail:597850470060392448> Ali 1 ")
                elif args == "2":
                    await ctx.send("<:gotojail:597850470060392448> Ali 2")
                elif args == "3":
                    await ctx.send("<:gotojail:597850470060392448> Ali 3")
                elif args == "4":
                    await ctx.send("<:gotojail:597850470060392448> Ali 4")
                else:
                    print(args[3:-1])
                    await ctx.send("<:gotojail:597850470060392448> Humza ")
            elif row[0] == "Ongoing":
                #Chooses which attack to do
                if args is None:
                    x = datetime.datetime.now() + timedelta(seconds=60)
                    #while ()
                    embed = discord.Embed(color=discord.Color.dark_red())
                    boss_hp = 10
                    hp = 15
                    embed.add_field(name="Goblin HP:", value=boss_hp, inline=False)
                    embed.add_field(name="HP:", value=hp, inline=False)
                    embed.add_field(name="Attacks: ", value="Attack 1\nHeal\nAttack 2\nHehe", inline=False)
                    embed.add_field(name="Previous Turn: ", value="xD")
                    embed.set_thumbnail(url="https://assets.stickpng.com/images/5b4eee54c051e602a568ce1b.png")
                    embed.set_footer(text=ctx.message.author.name, icon_url=ctx.message.author.avatar_url)
                    #msg = ctx.message.channel.send(embed=embed)
                    
                    msg = await ctx.message.channel.send(embed=embed)
                    await msg.add_reaction(self.client.get_emoji(788500845233700905))
                    await msg.add_reaction(self.client.get_emoji(788500845183631391))
                    await msg.add_reaction(self.client.get_emoji(788500845385482300))
                    await msg.add_reaction(self.client.get_emoji(788500845414580256))
                elif args == "1":
                    await ctx.send("<:gotojail:597850470060392448> Ali 1 ")
                elif args == "2":
                    await ctx.send("<:gotojail:597850470060392448> Ali 2")
                elif args == "3":
                    await ctx.send("<:gotojail:597850470060392448> Ali 3")
                elif args == "4":
                    await ctx.send("<:gotojail:597850470060392448> Ali 4")
                else:
                    print(args[3:-1])
                    await ctx.send("<:gotojail:597850470060392448> Humza ")
            elif row[0] == "Finished":
                await ctx.send("Done")
        else:            
            await ctx.send("You haven't !isekai yet!")
            # while boss_hp > 0:
            #     reaction, user = await self.client.wait_for('reaction_add', timeout=60.0)
            #     if str(reaction.emoji) == '<:1_:788500845233700905>' and user == ctx.message.author:
            #         await ctx.send('<:gotojail:597850470060392448> Ali ')
            #     elif str(reaction.emoji) == '<:2_:788500845183631391>' and user == ctx.message.author:
            #         await ctx.send('<:gotojail:597850470060392448> Humza ')
            #     elif str(reaction.emoji) == '<:3_:788500845385482300>' and user == ctx.message.author:
            #         await ctx.send('<:gotojail:597850470060392448> Fei ')
            #     elif str(reaction.emoji) == '<:4_:788500845414580256>' and user == ctx.message.author:
            #         await ctx.send('<:gotojail:597850470060392448> Ali 2')
            #     boss_hp = boss_hp - 1
            
            # embed.add_field(name="Goblin HP:", value=boss_hp, inline=False)
            # embed.add_field(name="HP:", value=hp)
            # embed.set_thumbnail(url="https://assets.stickpng.com/images/5b4eee54c051e602a568ce1b.png")
            # embed.set_footer(text=ctx.message.author.name, icon_url=ctx.message.author.avatar_url)
            # await msg.edit(embed=embed)
            
            # def check(reaction, user):
            #     return (user == ctx.message.author and str(reaction.emoji) == '<:1_:788500845233700905>') or (user == ctx.message.author and str(reaction.emoji) == '<:2_:788500845183631391>') or (user == ctx.message.author and str(reaction.emoji) == '<:3_:788500845385482300>') or (user == ctx.message.author and str(reaction.emoji) == '<:4_:788500845414580256>')
            # try:
            #     reaction, user = await self.client.wait_for('reaction_add', timeout=60.0, check=check)
            # except asyncio.TimeoutError:
            #     a = 3
            # else:
            #     while boss_hp > 0:
            #         if str(reaction.emoji) == '<:1_:788500845233700905>' and user == ctx.message.author:
            #             boss_hp = boss_hp - 10
            #             await ctx.send('<:gotojail:597850470060392448> Ali ')
            #         elif str(reaction.emoji) == '<:2_:788500845183631391>' and user == ctx.message.author:
            #             boss_hp = boss_hp - 7
            #             await ctx.send('<:gotojail:597850470060392448> Humza ')
            #         elif str(reaction.emoji) == '<:3_:788500845385482300>' and user == ctx.message.author:
            #             boss_hp = boss_hp - 3
            #             await ctx.send('<:gotojail:597850470060392448> Fei ')
            #         elif str(reaction.emoji) == '<:4_:788500845414580256>' and user == ctx.message.author:
            #             boss_hp = boss_hp - 1
            #             await ctx.send('<:gotojail:597850470060392448> Ali 2')
              
            #await ctx.send('React with <:1_:788500845233700905> <:2:788500845183631391> <:3:788500845385482300> or <:4_:788500845414580256> to call out a lolicon')
            # def check(reaction, user):
            #     return user == ctx.message.author and str(reaction.emoji) == '<:1_:788500845233700905>'
            # def check2(reaction, user):
            #     return user == ctx.message.author and str(reaction.emoji) == '<:2_:788500845183631391>'
            # def check3(reaction, user):
            #     return user == ctx.message.author and str(reaction.emoji) == '<:3_:788500845385482300>'
            # def check4(reaction, user):
            #     return user == ctx.message.author and str(reaction.emoji) == '<:4_:788500845414580256>'
            
            # try:
            #     

            # except asyncio.TimeoutError:
            #     #await ctx.send('👎')
            #     a = 3
            # else:
            #     await ctx.send('<:gotojail:597850470060392448> Ali ')
            # try:
            #     reaction, user = await self.client.wait_for('reaction_add', timeout=60.0, check=check2)

            # except asyncio.TimeoutError:
            #     #await ctx.send('👎')
            #     a = 3
            # else:
            #     await ctx.send('<:gotojail:597850470060392448> Humza')
            # try:
            #     reaction, user = await self.client.wait_for('reaction_add', timeout=60.0, check=check3)

            # except asyncio.TimeoutError:
            #     #await ctx.send('👎')
            #     a = 3
            # else:
            #     await ctx.send('<:gotojail:597850470060392448> Ali 2')
            # try:
            #     reaction, user = await self.client.wait_for('reaction_add', timeout=60.0, check=check4)

            # except asyncio.TimeoutError:
            #     #await ctx.send('👎')
            #     a = 3
            # else:
            #     await ctx.send('<:gotojail:597850470060392448> Humza 2')
            # if b == 1:
                
            # elif b == 2:
            #     try:
            #         reaction, user = await self.client.wait_for('reaction_add', timeout=60.0, check=check2)
            #     except asyncio.TimeoutError:
            #         #await ctx.send('👎')
            #         a = 3
            #     else:
            #         await ctx.send('<:gotojail:597850470060392448> <@!669979645004873758> 2')
            # elif b == 3:
            #     try:
            #         reaction, user = await self.client.wait_for('reaction_add', timeout=60.0, check=check3)

            #     except asyncio.TimeoutError:
            #         #await ctx.send('👎')
            #         a = 3
            #     else:
            #         await ctx.send('<:gotojail:597850470060392448> <@!669979645004873758> 3')
            # elif b == 4:
            #     try:
            #         reaction, user = await self.client.wait_for('reaction_add', timeout=60.0, check=check4)

            #     except asyncio.TimeoutError:
            #         #await ctx.send('👎')
            #         a = 3
            #     else:
            #         await ctx.send('<:gotojail:597850470060392448> <@!669979645004873758> 4')

            

def setup(client):
    client.add_cog(Battle(client))