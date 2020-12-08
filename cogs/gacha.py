import discord
import psycopg2
import random
import DiscordUtils
from config import config
from discord.ext import commands

class Gacha(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Inventory.py is ready')
    @commands.command()
    async def gdb(self, ctx, args):
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        args = str(args).lower()
        sql = """select count(*) from (select lower(unit) as unit from Gacha) as G where unit like %s;"""
        search = f'{args}'
        cur.execute(sql, (search,))
        print(cur.mogrify(sql, (search,)))
        rows = cur.fetchone()
        if rows[0] == 0:
            exact_match = False
        elif rows[0] == 1:
            exact_match = True
            sql = """select gunit, gacha_id from (select lower(unit) as gunit, gacha_id from Gacha) as A where gunit like %s;"""
            cur.execute(sql, (search,))
            rows= cur.fetchall()
            for r in rows:
                unit = r[0]
                g_gacha_id = r[1]
            #This query matches the lowercase gacha_id and compares it with the actual list
            cur.execute("select unit, rarity_id, unit_url, anime, rarity from Gacha where gacha_id = %s;", (g_gacha_id,))
            rows = cur.fetchall()
            for r in rows:
                g_unit = r[0]
                g_rarity = r[1]
                g_url = r[2]
                g_anime = r[3]
                g_rare = r[4]
            
            if g_rare == 'N':
                clr = discord.Color.default()
                t_url = "https://i.imgur.com/MkiU1ru.png"
            elif g_rare == 'R':
                clr = discord.Color.light_grey()
                t_url = "https://i.imgur.com/g4nD5jL.png"
            elif g_rare == 'SR':
                clr = discord.Color.orange()
                t_url = "https://i.imgur.com/xCUSAl5.png"
            elif g_rare == 'SSR':
                clr = discord.Color.red()
                t_url = "https://i.imgur.com/mZ9eHc3.png"
            elif g_rare == 'UR':
                clr = discord.Color.magenta()
                t_url = "https://i.imgur.com/Vp3Nwyw.png"
            embed = discord.Embed(
                color=clr                    
            )
            #select gunit, rarity_id, unit_url, anime from (select lower(unit) as gunit from Gacha) as A, Gacha where unit like 'keele%';
            embed.set_thumbnail(url=f"{t_url}")
            embed.set_image(url=f"{g_url}")
            embed.add_field(name=f"{g_unit}", value=f"Rarity: {self.client.get_emoji(g_rarity)}\nAnime: {g_anime}")
            await ctx.message.channel.send(embed=embed)
        if exact_match == False:
            sql = """select count(*) from (select lower(unit) as unit from Gacha) as G where unit like %s;"""
            search = f'%{args}%'
            cur.execute(sql, (search,))
            print(cur.mogrify(sql, (search,)))
            rows = cur.fetchall()
            for r in rows:
                count = r[0]
            if count == 0:
                await ctx.send("There exists no such unit currently")
            elif count == 1:
                #query checks to see the unit in lowercase returning the unit and id (Should only be 1)
                sql = """select gunit, gacha_id from (select lower(unit) as gunit, gacha_id from Gacha) as A where gunit like %s;"""
                cur.execute(sql, (search,))
                rows= cur.fetchall()
                for r in rows:
                    unit = r[0]
                    g_gacha_id = r[1]
                #This query matches the lowercase gacha_id and compares it with the actual list
                cur.execute("select unit, rarity_id, unit_url, anime, rarity from Gacha where gacha_id = %s;", (g_gacha_id,))
                rows = cur.fetchall()
                for r in rows:
                    g_unit = r[0]
                    g_rarity = r[1]
                    g_url = r[2]
                    g_anime = r[3]
                    g_rare = r[4]
                
                if g_rare == 'N':
                    clr = discord.Color.default()
                    t_url = "https://i.imgur.com/MkiU1ru.png"
                elif g_rare == 'R':
                    clr = discord.Color.light_grey()
                    t_url = "https://i.imgur.com/g4nD5jL.png"
                elif g_rare == 'SR':
                    clr = discord.Color.orange()
                    t_url = "https://i.imgur.com/xCUSAl5.png"
                elif g_rare == 'SSR':
                    clr = discord.Color.red()
                    t_url = "https://i.imgur.com/mZ9eHc3.png"
                elif g_rare == 'UR':
                    clr = discord.Color.magenta()
                    t_url = "https://i.imgur.com/Vp3Nwyw.png"
                embed = discord.Embed(
                    color=clr                    
                )
                #select gunit, rarity_id, unit_url, anime from (select lower(unit) as gunit from Gacha) as A, Gacha where unit like 'keele%';
                embed.set_thumbnail(url=f"{t_url}")
                embed.set_image(url=f"{g_url}")
                embed.add_field(name=f"{g_unit}", value=f"Rarity: {self.client.get_emoji(g_rarity)}\nAnime: {g_anime}")
                await ctx.message.channel.send(embed=embed)
            else:
                embed = discord.Embed(color=discord.Color.blurple())
                sql = """select gunit, gacha_id from (select lower(unit) as gunit, gacha_id from Gacha) as A where gunit like %s;"""
                cur.execute(sql, (search,))
                rows= cur.fetchall()
                nums = []
                search_display = ""
                for r in rows:
                    nums.append(r[1])
                for i in nums:
                    cur.execute("select unit, rarity_id, unit_url, anime from Gacha where gacha_id = %s;", (i,))
                    rows = cur.fetchone()
                    search_display += f"**{rows[0]}** - {rows[3]}\n"
                # sql = """select unit, rarity_id, unit_url, anime from Gacha where unit like %s;"""
                # cur.execute(sql, (search,))
                # #cur.execute("select gunit, rarity_id, unit_url, anime from (select lower(unit) as gunit from Gacha) as A, Gacha where unit like %s%%;", (args,))
                # rows=cur.fetchall()
                print(f"Search: {search_display}")
                embed.add_field(name=f"Found {len(nums)} results", value=f"\n{search_display}")
                await ctx.message.channel.send(embed=embed)
    @commands.command()
    async def sugoinfo(self, ctx):
        embed = discord.Embed(color=discord.Color.blue())
        embed.add_field(name="Gacha News", value=f"Currently still a WIP but a ** new batch** has been added so have fun.\n\
            \nGive me some good images tho, most of em succ but make sure they're good dimensions. Anime planet ones got good dimensions but the pics are trash. Search !gdb sham for when dimensions go wrong {self.client.get_emoji(356789072062316544)}\
            \n\n**NOTE:** Keep in mind your box will _**reset**_ after I finish ironing out issues and testing stuff so don't get too attached")
        await ctx.message.channel.send(embed=embed)

    @commands.command()
    async def h1(self, ctx):
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
            
            rng = random.randint(1, 100)
            if (rng == 1):
                cur.execute("select unit, rarity_id, unit_url, anime, gacha_id, rarity from Gacha where rarity = 'UR' order by random() limit 1;")
                rows= cur.fetchall()
                for r in rows:
                    g_unit = r[0]
                    g_rarity = r[1]
                    g_url = r[2]
                    g_anime = r[3]
                    g_gacha_id = r[4]
                    g_rare = r[5]
            elif rng <= 5 and rng > 1:
                cur.execute("select unit, rarity_id, unit_url, anime, gacha_id, rarity from Gacha where rarity = 'SSR' order by random() limit 1;")
                rows= cur.fetchall()
                for r in rows:
                    g_unit = r[0]
                    g_rarity = r[1]
                    g_url = r[2]
                    g_anime = r[3]
                    g_gacha_id = r[4]
                    g_rare = r[5]
            elif rng <= 30 and rng > 5:
                cur.execute("select unit, rarity_id, unit_url, anime, gacha_id, rarity from Gacha where rarity = 'SR' order by random() limit 1;")
                rows= cur.fetchall()
                for r in rows:
                    g_unit = r[0]
                    g_rarity = r[1]
                    g_url = r[2]
                    g_anime = r[3]
                    g_gacha_id = r[4]
                    g_rare = r[5]
            elif rng <= 60 and rng > 30:
                cur.execute("select unit, rarity_id, unit_url, anime, gacha_id, rarity from Gacha where rarity = 'R' order by random() limit 1;")
                rows= cur.fetchall()
                for r in rows:
                    g_unit = r[0]
                    g_rarity = r[1]
                    g_url = r[2]
                    g_anime = r[3]
                    g_gacha_id = r[4]
                    g_rare = r[5]
            elif rng <= 100 and rng > 60:
                cur.execute("select unit, rarity_id, unit_url, anime, gacha_id, rarity from Gacha where rarity = 'N' order by random() limit 1;")
                rows= cur.fetchall()
                for r in rows:
                    g_unit = r[0]
                    g_rarity = r[1]
                    g_url = r[2]
                    g_anime = r[3]
                    g_gacha_id = r[4]
                    g_rare = r[5]
            cur.execute("insert into Player_Gacha_Inventory(discord_id, unit, gacha_id) values (%s, %s, %s);", (ctx.message.author.id, g_unit, g_gacha_id))
            if g_rare == 'N':
                clr = discord.Color.default()
                t_url = "https://i.imgur.com/MkiU1ru.png"
            elif g_rare == 'R':
                clr = discord.Color.light_grey()
                t_url = "https://i.imgur.com/g4nD5jL.png"
            elif g_rare == 'SR':
                clr = discord.Color.orange()
                t_url = "https://i.imgur.com/xCUSAl5.png"
            elif g_rare == 'SSR':
                clr = discord.Color.red()
                t_url = "https://i.imgur.com/mZ9eHc3.png"
            elif g_rare == 'UR':
                clr = discord.Color.magenta()
                t_url = "https://i.imgur.com/Vp3Nwyw.png"
            embed = discord.Embed(
                title="H1 Pull",
                color=clr                    
            )
            for x in g_anime:
                print(x)
            embed.set_thumbnail(url=f"{t_url}")    
            embed.set_image(url=f"{g_url}")
            embed.add_field(name=f"{g_unit}", value=f"Rarity: {self.client.get_emoji(g_rarity)}\nAnime: {g_anime}")
            embed.set_footer(text=f"{ctx.message.author.name}", icon_url=f"{ctx.message.author.avatar_url}")
            await ctx.message.channel.send(embed=embed)
        else:
            await ctx.send("Sir you haven't !isekai yet")
        cur.close()
        conn.commit()
        conn.close()
    @commands.command()
    async def h10(self, ctx):
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
            h10 = ""
            for i in range(0,10):
                rng = random.randint(1, 100)
                if (rng == 1):
                    cur.execute("select unit, rarity_id, gacha_id from Gacha where rarity = 'UR' order by random() limit 1;")
                    rows = cur.fetchall()
                    for r in rows:
                        h10 += f"{self.client.get_emoji(r[1])} **{r[0]}** {self.client.get_emoji(r[1])}\n"
                        cur.execute("insert into Player_Gacha_Inventory(discord_id, unit, gacha_id) values (%s, %s, %s);", (ctx.message.author.id, r[0], r[2]))
                elif rng <= 5 and rng > 1:
                    cur.execute("select unit, rarity_id, gacha_id from Gacha where rarity = 'SSR' order by random() limit 1;")
                    rows = cur.fetchall()
                    for r in rows:
                        h10 += f"{self.client.get_emoji(r[1])} **{r[0]}**\n"
                        cur.execute("insert into Player_Gacha_Inventory(discord_id, unit, gacha_id) values (%s, %s, %s);", (ctx.message.author.id, r[0], r[2]))
                elif rng <= 30 and rng > 5:
                    cur.execute("select unit, rarity_id, gacha_id from Gacha where rarity = 'SR' order by random() limit 1;")
                    rows = cur.fetchall()
                    for r in rows:
                        h10 += f"{self.client.get_emoji(r[1])} {r[0]}\n"
                        cur.execute("insert into Player_Gacha_Inventory(discord_id, unit, gacha_id) values (%s, %s, %s);", (ctx.message.author.id, r[0], r[2]))
                elif rng <= 60 and rng > 30:
                    cur.execute("select unit, rarity_id, gacha_id from Gacha where rarity = 'R' order by random() limit 1;")
                    rows = cur.fetchall()
                    for r in rows:
                        h10 += f"{self.client.get_emoji(r[1])} {r[0]}\n"
                        #print(r[0])
                        #((ctx.message.author.id,), (r[0],), (r[2],))
                        cur.execute("insert into Player_Gacha_Inventory(discord_id, unit, gacha_id) values (%s, %s, %s);", (ctx.message.author.id, r[0], r[2]))
                elif rng <= 100 and rng > 60:
                    cur.execute("select unit, rarity_id, gacha_id from Gacha where rarity = 'N' order by random() limit 1;")
                    rows = cur.fetchall()
                    for r in rows:
                        h10 += f"{self.client.get_emoji(r[1])} {r[0]}\n"
                        cur.execute("insert into Player_Gacha_Inventory(discord_id, unit, gacha_id) values (%s, %s, %s);", (ctx.message.author.id, r[0], r[2]))
                print(i)
            # ur = self.client.get_emoji(784587909495128066)
            # ssr = self.client.get_emoji(784587928667029554)
            # sr = self.client.get_emoji(784587938846867493)
            # r = self.client.get_emoji(784587951479848994)
            # n = self.client.get_emoji(784587962037829662)
            await ctx.message.channel.send(f"**H1 Gacha Multi** - {ctx.message.author.name}\n{h10}")
        else:
            await ctx.send("Sir you haven't !isekai yet")
        cur.close()
        conn.commit()
        conn.close()
def setup(client):
    client.add_cog(Gacha(client))