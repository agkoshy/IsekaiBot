select unit, r_id, num, ord_id
from
    (select distinct I.unit as  unit, G.rarity_id as r_id, count(*) as num
    from Gacha G, Player_Gacha_Inventory I
    where G.gacha_id = I.gacha_id 
    and I.discord_id = 135151849320873986 
    group by I.unit, G.rarity_id 
    having count(*) > 0 
    limit 15 
    offset 0) D
inner join Rarity R on D.r_id = R.rarity_id
order by ord_id;