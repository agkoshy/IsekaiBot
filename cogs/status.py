import discord
import psycopg2
import random
from config import config
from discord.ext import commands


class Status(commands.Cog):

    def __init__(self, client):
        self.client = client 

    @commands.Cog.listener()
    async def on_ready(self):
        print('Status.py is ready')
    @commands.command()
    async def stats(self, ctx):
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("select discord_id from Player;")
        rows = cur.fetchall()
        player_exist = True
        for r in rows:
            if r[0] == 0:
                player_exist = False
        if player_exist == True:
            cur.execute("select str, intl, dex, vit, wis, eva, crit, acc from Player_Stats where discord_id = %s;", (ctx.message.author.id,))
            row = cur.fetchone()
            sth = row[0]
            intl = row[1]
            dex = row[2]
            vit = row[3]
            wis = row[4]
            eva = row[5]
            crit = row[6]
            acc = row[7]
            
            equipments = ["helm", "chest", "pants", "boots", "gloves", "necklace", "ring", "cape", "weapon", "offhand_weapon"]
            i = 0
            add_sth = 0
            add_intl = 0
            add_dex = 0
            add_vit = 0
            add_wis = 0
            add_eva = 0
            add_crit = 0
            add_acc = 0
            add_crit_multi = 0
            while (i < len(equipments)):
                #Gives me equipment name per slot
                cur.execute(f"select {equipments[i]} from Player_Gear where discord_id = {ctx.message.author.id};")
                gear_name_row = cur.fetchone()
                if gear_name_row[0] is not None:
                    print("no")
                else: 
                    print("yes")
                #Gets me all the stats for said equipment
                if gear_name_row[0] is not None:
                    cur.execute("select str, intl, dex, vit, wis, eva, crit, acc, crit_multi from Gear_Stats where gear = %s;", (gear_name_row[0],))
                    add_row = cur.fetchone() 
                    add_sth += add_row[0]
                    add_intl += add_row[1]
                    add_dex += add_row[2]
                    add_vit += add_row[3]
                    add_wis += add_row[4]
                    add_eva += add_row[5]
                    add_crit += add_row[6]
                    add_acc += add_row[7]
                    add_crit_multi += add_row[8]         
                i = i + 1
            embed = discord.Embed(color=1752220)
            embed.add_field(name="Stats", value=f"**STR:** {sth+add_sth} (+{add_sth})\nINT: {intl+add_intl} (+{add_intl})\nDEX: {dex+add_dex} (+{add_dex})\nVIT: {vit+add_vit} (+{add_vit})\nWIS: {wis+add_wis} (+{add_wis})\nEVA: {eva+add_eva}% (+{add_eva}%)\nCRIT: {crit+add_crit}% (+{add_crit}%)\nACC: {acc+add_acc}% (+{add_acc}%)\n")
            embed.set_author(name=ctx.message.author.name, icon_url=ctx.message.author.avatar_url)
            embed.set_footer(text="(+X) is total stats from Gear Equipped")
            await ctx.message.channel.send(embed=embed)

            
        cur.close()
        conn.commit()
        conn.close() 
    @commands.command()
    async def status(self, ctx):
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
            cur.execute("select * from Player where discord_id = %s;", (ctx.message.author.id,))
            rows = cur.fetchall()
            print(rows)
            for r in rows:
                id = r[0]
                gold = r[1]
                adv = r[2]
                lvl = r[3]
                p_exp = r[4]
            cur.execute("select ex from Lvl where lvl = %s;", (lvl,))
            r = cur.fetchone()
            statusEmbed = discord.Embed(
                colour = 1752220
            )
            in_adv = "Currently in dungeon"
            if adv is None:
                in_adv = "Not in dungeon"
            statusEmbed.add_field(name="Status", value=f"Name: {ctx.message.author.name}\nLevel: {lvl}\nExp: {p_exp}/{r[0]}\nGold: {gold}\nDungeon Status: {in_adv}")
            print(ctx.message.author.avatar_url)
            statusEmbed.set_thumbnail(url=f"{ctx.message.author.avatar_url}")
            await ctx.send(embed=statusEmbed)
        else:
            await ctx.send("Sir you haven't !isekai yet")
        cur.close()
        conn.close()


def setup(client):
    client.add_cog(Status(client))