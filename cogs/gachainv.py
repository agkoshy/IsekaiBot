import discord
import psycopg2
import random
import DiscordUtils
from config import config
from discord.ext import commands

class GachaInv(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('GachaInv.py is ready')

    @commands.command()
    async def cbox(self, ctx):
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
            cur.execute("select count(*) from (select distinct gacha_id, count(*) from Player_Gacha_Inventory where discord_id = %s group by gacha_id) as foo;", (ctx.message.author.id,))
            rows = cur.fetchall()
            count = 0
            for r in rows:
                count_if_zero = r[0]
                count = r[0]/15
            print(f"count: {count_if_zero}")
            if count_if_zero != 0:
                embeds = []
                for x in range(0, int(count+1)):
                    print(x)
                    cur.execute("select unit, r_id, num, ord_id from (select distinct I.unit as unit, G.rarity_id as r_id, count(*) as num from Gacha G, Player_Gacha_Inventory I where G.gacha_id = I.gacha_id and I.discord_id = %s group by I.unit, G.rarity_id having count(*) > 0) D inner join Rarity R on D.r_id = R.rarity_id order by r.ord_id limit 15 offset %s;", (ctx.message.author.id, int(15*x)))
                    rows = cur.fetchall()
                    inv_list = ""        
                    for r in rows:
                        if r[2] > 1:
                            inv_list += f"{self.client.get_emoji(r[1])} {r[0]} (x{r[2]})\n"
                        else:
                            inv_list += f"{self.client.get_emoji(r[1])} {r[0]}\n"
                    embeds.append(discord.Embed(color=discord.Color.dark_purple()).add_field(name=f"Page {int(x+1)}", value=f"{inv_list}").set_author(name=f"{ctx.message.author.name}",icon_url=f"{ctx.message.author.avatar_url}"))
                # cur.execute("select unit, rarity_id from Gacha order by gacha_id limit 15;")
                # rows = cur.fetchall()
                # inv_list = ""        
                # for r in rows:
                #     inv_list += f"{self.client.get_emoji(r[1])} {r[0]}\n"
                # embed1 = discord.Embed(color=ctx.author.color).add_field(name="** **", value=f"{inv_list}"
                # )
                # cur.execute("select unit, rarity_id from Gacha order by gacha_id limit 15 offset 15;")
                # rows = cur.fetchall()
                # inv_list = ""        
                # for r in rows:
                #     inv_list += f"{self.client.get_emoji(r[1])} {r[0]}\n"
                # embed2 = discord.Embed(color=ctx.author.color).add_field(name="Example2", value=f"{inv_list}")
                # cur.execute("select unit, rarity_id from Gacha order by gacha_id limit 15 offset 30;")
                # rows = cur.fetchall()
                # inv_list = ""        
                # for r in rows:
                #     inv_list += f"{self.client.get_emoji(r[1])} {r[0]}\n"
                # embed3 = discord.Embed(color=ctx.author.color).add_field(name="Example3", value=f"{inv_list}")
                paginator = DiscordUtils.Pagination.AutoEmbedPaginator(ctx)
                await paginator.run(embeds)
            else:
                await ctx.send("You have no units")
            # ur = self.client.get_emoji(784587909495128066)
            # ssr = self.client.get_emoji(784587928667029554)
            # sr = self.client.get_emoji(784587938846867493)
            # r = self.client.get_emoji(784587951479848994)
            # n = self.client.get_emoji(784587962037829662)
            # await ctx.message.channel.send(f"{ur} {ssr} {sr} {r} {n}")
        else:
            await ctx.send("Sir, you haven't !isekai yet")
        cur.close()
        conn.close()
def setup(client):
    client.add_cog(GachaInv(client))