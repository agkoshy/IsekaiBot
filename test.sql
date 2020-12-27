insert into Boss (boss, boss_race, hp, exp_drop, descr, lvl_req) values
    ('Goblin', 'Goblin', 60, 4, 'A primitive and savage monster representing the basest desires of their creator, Demon Lord Humza', 1),
    ('Small Slime', 'Slime', 50, 3, 'A small goop like creature. Legends say that the Ape King Fei''s first monster was this', 1),
    ('Horned Rabbit', 'Rabbit', 45, 4, 'A rabbit creature with a horn growing out of its head. ', 1),
    ('Slime', 'Slime', 150, 10, 'A rabbit creature with a horn growing out of its head. ', 4),
    ('Lesser Wolf', 'Wolf', 120, 8, 'A small wolf monster capable of inflicting bleed', 4);

-- insert into Classes (adv_class, main_class, level_req, prev_adv, tame) values
--     ('Villager', 'Villager',,''),
--     ('Warrior', 'Warrior', 10, 'Villager'),
--     ('Mage', 'Mage', 10, 'Villager'),
--     ('Ranger', 'Ranger', 10, 'Villager'),
--     ('Novice Fighter', 'Warrior', 20, 'Warrior'),
--     ('Novice Swordsman', 'Warrior', 20, 'Warrior'),
--     ('Squire', 'Warrior', 20, 'Warrior'),
--     ('Experienced Squire', 'Warrior', 30, 'Squire'),
--     ('Intermediate Fighter', 'Warrior', 30, 'Novice Fighter'),
--     ('Greatswordsman', 'Warrior', 30, 'Swordsman'),
--     ('Dualwielder', 'Warrior', 30, 'Swordsman'),
--     ('Novice Fire Mage', 'Mage', 20, 'Mage'),
--     ('Novice Water Mage', 'Mage', 20, 'Mage'),
--     ('Novice Earth Mage', 'Mage', 20, 'Mage'),
--     ('Novice Wind Mage', 'Mage', 20, 'Mage'),
--     ('Intermediate Fire Mage', 'Mage', 30, 'Novice Fire Mage'),
--     ('Intermediate Water Mage', 'Mage', 30, 'Novice Water Mage'),
--     ('Intermediate Earth Mage', 'Mage', 30, 'Novice Earth Mage'),
--     ('Intermediate Fire Mage', 'Mage', 30, 'Novice Fire Mage'),
--     ('Scout', 'Ranger', 20, 'Ranger'),
--     ('Rogue', 'Ranger', 20, 'Ranger'),
--     ('Spearwielder', 'Ranger', 20, 'Ranger'),
--     ('Novice Archer', 'Ranger', 30, 'Scout'),
--     ('Hunter', 'Ranger', 30, 'Scout'),
--     ('Thief', 'Ranger', 30, 'Rogue'),
--     ('Assassin', 'Ranger', 30, 'Rogue'),
--     ('Intermediate Spearwielder', 'Ranger', 30, 'Spearwielder'),
--     ('Polearmwielder', 'Ranger', 30, 'Spearwielder');

-- create table Classes (
--     main_class  varchar(300),
--     adv_class   varchar(300),
--     constraint Classes_PK
--         primary key (adv_class)
-- );

-- add constraint Player_FK_Boss
-- -- foreign key(boss) references Boss(boss);
-- alter table Classes
-- add column level_req int,
-- add column prev_adv varchar(300);
-- add column boss_hp int,
-- add column title varchar(300),
-- add column game_state varchar(300);