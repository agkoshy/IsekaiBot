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
                #cur.execute("insert into Player_Gamestate (discord_id, debuffs, elemental_type, elemental_damage, elemental_text, ) values into (%s);", (ctx.message.author.id,))
                if args is None:
                    x = datetime.datetime.now() + timedelta(seconds=60)
                    #while ()
                    cur.execute("select boss from Player where discord_id = %s;", (ctx.message.author.id,))
                    boss_name = cur.fetchone()
                    cur.execute("select hp, boss_thumbnail from Boss where boss  = %s;", (boss_name[0],))
                    boss_hp = cur.fetchone()
                    cur.execute("select move_one, move_two, move_three, move_four from Player_Moves where discord_id = %s;", (ctx.message.author.id,))
                    player_move = cur.fetchone()
                    embed = discord.Embed(color=discord.Color.dark_red())
                    hp = 10
                    embed.add_field(name=f"{boss_name[0]} HP:", value=boss_hp[0], inline=False)
                    embed.add_field(name="HP:", value=hp, inline=False)
                    embed.add_field(name="Attacks: ", value=f"{player_move[0]}\n{player_move[1]}\n{player_move[2]}\n{player_move[3]}")
                    embed.set_thumbnail(url=f"{boss_hp[1]}")
                    embed.set_footer(text=ctx.message.author.name, icon_url=ctx.message.author.avatar_url)
                    #msg = ctx.message.channel.send(embed=embed)
                    
                    msg = await ctx.message.channel.send(embed=embed)
                    # await msg.add_reaction(self.client.get_emoji(788500845233700905))
                    # await msg.add_reaction(self.client.get_emoji(788500845183631391))
                    # await msg.add_reaction(self.client.get_emoji(788500845385482300))
                    # await msg.add_reaction(self.client.get_emoji(788500845414580256))
                elif args == "1" or args == "2" or args == "3" or args == "4":
                    if args == "1":
                        move = "move_one"
                    elif args == "2":
                        move = "move_two"
                    elif args == "3":
                        move = "move_three"
                    elif args == "4":
                        move = "move_four"
                    print(move)
                    cur.execute(f"select {move} from Player_Moves where discord_id = {ctx.message.author.id}")
                    row = cur.fetchone()
                    move_one = row[0]
                    cur.execute("select move_name, move_descr, move_type, lvl_req, base_dmg, scaling_dmg, stat_type, weapon_type, elemental_type, \
                        elemental_chance, elemental_dmg, elemental_text, off_elemental_type, off_elemental_chance, off_elemental_dmg, off_elemental_text,\
                            move_pretext, move_posttext, preskip, pre_text, postskip, post_text, mp_cost from Usermoves where move_name = %s;", (move_one,))
                    r = cur.fetchone()
                    print(r)
                    move_name = r[0]
                    move_descr = r[1]
                    move_type = r[2]
                    lvl_req = r[3]
                    base_dmg = r[4]
                    scaling_dmg = r[5]
                    stat_type = r[6]
                    weapon_type = r[7]
                    elemental_type = r[8]
                    elemental_chance = r[9]
                    elemental_dmg = r[10]
                    elemental_text = r[11]
                    off_elemental_type = r[12]
                    off_elemental_chance = r[13]
                    off_elemental_dmg = r[14]
                    off_elemental_text = r[15]
                    move_pretext = r[16]
                    move_posttext = r[17]
                    preskip = r[18]
                    pre_text = r[19]
                    postskip = r[20]
                    post_text = r[21]
                    mp_cost = r[22]

                    cur.execute("select str, intl, dex, vit, eva, wis, crit, acc from Player_Stats where discord_id = %s;", (ctx.message.author.id,))
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
                            cur.execute("select str, intl, dex, vit, eva, wis, crit, acc, crit_multi from Gear_Stats where gear = %s;", (gear_name_row[0],))
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
                        
                    print(f"add str {sth + add_sth} add int {intl + add_intl} add dex {dex + add_dex} add vit {vit + add_vit} add wis {wis + add_wis} add eva {eva + add_eva} add crit {crit + add_crit} add acc {acc + add_acc} add crit m {add_crit_multi}")
                    rng_acc = random.randint(1,100)
                    rng_crit = random.randint(1,100)
                    if move_type == "Physical" or move_type == "Magical" or move_type == "Speed":                          
                        if rng_acc <= acc:
                            if rng_crit <= crit:
                                if stat_type == "str":
                                    dmg = (base_dmg + ((scaling_dmg/100)*sth))*1.5
                                elif stat_type == "intl":
                                    dmg = (base_dmg + ((scaling_dmg/100)*intl))*1.5
                                elif stat_type == "dex":
                                    dmg = (base_dmg + ((scaling_dmg/100)*dex))*1.5                            
                            else:
                                if stat_type == "str":
                                    dmg = base_dmg + ((scaling_dmg/100)*sth)
                                elif stat_type == "intl":
                                    dmg = base_dmg + ((scaling_dmg/100)*intl)
                                elif stat_type == "dex":
                                    dmg = base_dmg + ((scaling_dmg/100)*dex)
                            rng_elem = random.randint(1,100)
                            #print(rng_elem)
                            #print(elemental_chance)
                            if rng_elem <= elemental_chance:
                                elem_dmg = elemental_dmg
                                print(f"{elemental_text}")
                            print(f"{move_pretext} {dmg} {move_posttext}")
                                # if elemental_type == "Burn":
                                #     print(f"Burn applied and takes {elemental_dmg}")
                                # if elemental_type == "Wet":
                                #     print(f"Wet applied and takes {elemental_dmg}")
                                # if elemental_type == "Wind":
                                #     print(f"Wind applied and takes {elemental_dmg}")
                                # if elemental_type == "Earth":
                                #     print(f"Earth applied and takes {elemental_dmg}")
                                # if elemental_type == "Bleed":
                                #     print(f"Bleed applied and takes {elemental_dmg}")
                                # if elemental_type == "Poison":
                                #     print(f"Poison applied and takes {elemental_dmg}")
                                # if elemental_type == "Chill":
                                #     print(f"Chill applied and takes {elemental_dmg}")
                                # if elemental_type == "Electro":
                                #     print(f"Electro applied and takes {elemental_dmg}")
                                # if elemental_type == "Light":
                                #     print(f"Light applied and takes {elemental_dmg}")   
                                # if elemental_type == "Dark":
                                #     print(f"Dark applied and takes {elemental_dmg}")
                        else:
                            dmg = 0
                    elif move_type == "Heal":
                        if rng_acc <= acc:
                            if rng_crit <= crit:
                                if stat_type == "str":
                                    hp = (base_dmg + ((scaling_dmg/100)*sth))*1.5
                                elif stat_type == "intl":
                                    hp = (base_dmg + ((scaling_dmg/100)*intl))*1.5
                                elif stat_type == "dex":
                                    hp = (base_dmg + ((scaling_dmg/100)*dex))*1.5                            
                            else:
                                if stat_type == "str":
                                    hp = base_dmg + ((scaling_dmg/100)*sth)
                                elif stat_type == "intl":
                                    hp = base_dmg + ((scaling_dmg/100)*intl)
                                elif stat_type == "dex":
                                    hp = base_dmg + ((scaling_dmg/100)*dex)
                            rng_elem = random.randint(1,100)
                            if rng_elem <= elemental_chance:
                                elem_dmg = elemental_dmg
                                print(f"{elemental_text}")
                        else:
                            hp = 0
                    cur.execute("select boss from Player where discord_id = %s;", (ctx.message.author.id,))
                    boss_name = cur.fetchone()
                    cur.execute("select hp from Boss where boss  = %s;", (boss_name[0],))
                    boss_hp = cur.fetchone()
                    cur.execute("select count(*) from bossmoves where boss = %s;", (boss_name[0],))
                    boss_attack_count = cur.fetchone()
                    cur.execute("select move_name, damage, move_text, elemental_type, elemental_chance, elemental_timer, elemental_name, off_elemental_type, off_elemental_chance, off_elemental_timer, off_elemental_name, preskip, postskip from BossMoves where boss = %s;", (boss_name[0],))
                    row = cur.fetchall()
                    rng_boss_attack_count = random.randint(1, boss_attack_count[0])
                    # print(rng_boss_attack_count)
                    # print(row)
                    r = row[rng_boss_attack_count-1]
                    boss_move = r[0]
                    boss_dmg = r[1]
                    boss_text = r[2]
                    boss_ele_type = r[3]
                    boss_ele_chance = r[4]
                    boss_ele_timer = r[5]
                    boss_ele_text = r[6]
                    boss_off_ele_type = r[7]
                    boss_off_ele_chance = r[8]
                    boss_off_ele_timer = r[9]
                    boss_off_ele_text = r[10]
                    boss_preskip = r[11]
                    boss_postskip = r[12]
                    
                    #cur.execute("update Player_Gamestate set where discord_id = %s")
                    print(f"Boss Move: {boss_move}")
                    print(dmg)
                    print(boss_dmg)
                #     #await ctx.send("<:gotojail:597850470060392448> Ali 1 ")
                # elif args == "2":
                #     await ctx.send("<:gotojail:597850470060392448> Ali 2")
                # elif args == "3":
                #     await ctx.send("<:gotojail:597850470060392448> Ali 3")
                # elif args == "4":
                #     await ctx.send("<:gotojail:597850470060392448> Ali 4")
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