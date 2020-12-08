create table Lvl (
    lvl        int not null,
    ex         int not null,
    constraint Lvl_PK
        primary key (lvl)  
);
create table Player (
    discord_id  bigint not null,
    p_money     bigint not null,
    adv         timestamp,
    lvl         int    not null,
    p_exp       int    not null,
    constraint User_PK
        primary key(discord_id),
    constraint Lvl_FK_lvl
        foreign key (lvl) references Lvl(lvl)
);
create table Gacha (
    gacha_id    int not null,
    unit        varchar(300) not null,
    descr       varchar(300),
    rarity      varchar(5),
    rarity_id   bigint,
    unit_url    varchar(3000),
    anime       varchar(3000),
    constraint Gacha_PK
        primary key(gacha_id)
);
create table Gear (
    gear_id    int         not null,
    gear       varchar(300) not null,
    descr      varchar(300) not null,
    equiptype  varchar(15) not null,
    rarity     varchar(15) not null,
    gold       int         not null,
    constraint Gear_PK
        primary key (gear_id),
    constraint Gear_Name_UNIQ
        unique(gear)
);

create table Boss (
    boss      varchar(30) not null,
    descr     varchar(300) not null,
    constraint Boss_PK
        primary key (boss)
);

create table Loot (
    boss      varchar(30) not null,
    gear      int not null,
    constraint Loot_PK
        primary key (boss, gear),
    constraint Loot_FK_Boss
        foreign key (boss) references Boss(boss),
    constraint Loot_FK_Gear
        foreign key (gear) references Gear(gear_id)
);

create table Player_Gacha_Inventory (
    discord_id  bigint  not null,
    unit        varchar(300) not null,
    gacha_id    int not null,
    constraint Player_Gacha_Inventory_FK_dID
        foreign key (discord_id) references Player(discord_id)
);
insert into Rarity (rarity, rarity_id, ord_id) values
    ('UR', 784587909495128066, 1),
    ('SSR', 784587928667029554, 2),
    ('SR', 784587938846867493, 3),
    ('R', 784587951479848994, 4),
    ('N', 784587962037829662, 5);

insert into Gear (gear_id, gear, descr, equiptype, rarity, gold) values
    (1, 'Goblin Slayer Helm', 'The helmet of an expert in slaying goblins', 'Helmet', 'D', 50),
    (2, 'Bloodied Shortsword', 'The shortsword of a dead adventure', 'Weapon', 'F', 1),
    (3, 'Leather Chest', 'A flexible chest made out of monster leather', 'Chest', 'E', 3),
    (4, 'Torch', 'An item to light the way', 'Weapon', 'F', 1),
    (5, 'Villager Garb', 'A flexible chest made out of monster leather', 'Chest', 'E', 3),
    (6, 'Farming Gloves', 'A flexible chest made out of monster leather', 'Chest', 'E', 3),
    (7, 'Farming Hoe', 'A flexible chest made out of monster leather', 'Chest', 'E', 3),
    (8, 'Farmers Pitchfork', 'A flexible chest made out of monster leather', 'Chest', 'E', 3),
    (9, 'Villager Boots', 'A flexible chest made out of monster leather', 'Chest', 'E', 3),
    (10, 'Villager Belt', 'A flexible chest made out of monster leather', 'Chest', 'E', 3),
    (11, 'A', 'A flexible chest made out of monster leather', 'Chest', 'E', 3),
    (12, 'B', 'A flexible chest made out of monster leather', 'Chest', 'E', 3),
    (13, 'C', 'A flexible chest made out of monster leather', 'Chest', 'E', 3),
    (14, 'D', 'A flexible chest made out of monster leather', 'Chest', 'E', 3),
    (15, 'E', 'A flexible chest made out of monster leather', 'Chest', 'E', 3),
    (16, 'F', 'A flexible chest made out of monster leather', 'Chest', 'E', 3),
    (17, 'G', 'A flexible chest made out of monster leather', 'Chest', 'E', 3),
    (18, 'H', 'A flexible chest made out of monster leather', 'Chest', 'E', 3),
    (19, 'I', 'A flexible chest made out of monster leather', 'Chest', 'E', 3),
    (20, 'J', 'A flexible chest made out of monster leather', 'Chest', 'E', 3),
    (21, 'K', 'A flexible chest made out of monster leather', 'Chest', 'E', 3),
    (22, 'L', 'A flexible chest made out of monster leather', 'Chest', 'E', 3),
    (23, 'M', 'A flexible chest made out of monster leather', 'Chest', 'E', 3),
    (24, 'N', 'A flexible chest made out of monster leather', 'Chest', 'E', 3),
    (25, 'O', 'A flexible chest made out of monster leather', 'Chest', 'E', 3),
    (26, 'P', 'A flexible chest made out of monster leather', 'Chest', 'E', 3),
    (27, 'Q', 'A flexible chest made out of monster leather', 'Chest', 'E', 3);

insert into Boss (boss, descr) values 
    ('Hobgoblin', 'The evolved version of a regular goblin. Has above average strength.');

insert into Loot (boss, gear) values
    ('Hobgoblin', 1),
    ('Hobgoblin', 2),
    ('Hobgoblin', 4);

insert into Lvl (lvl, ex) values
    (1, 100),
    (2, 700);

insert into Player (discord_id, p_money, adv, lvl, p_exp) values
    (1, 0, '2020-12-03 22:50:42', 1, 0);

insert into Gacha(gacha_id, unit, descr, rarity, unit_url, anime) values
    (1, 'Aqua', 'Sample Description here', 'UR', 'https://www.anime-planet.com/images/characters/thumbs/aqua-72066.jpg?t=1561832601', 'Kono Subarashii Sekai ni Shukufuku wo!'),
    (2, 'Angel', 'Sample Description here', 'R', 'https://www.anime-planet.com/images/characters/thumbs/angel-konosuba-gods-blessing-on-this-wonderful-world-101876.jpg?t=1457994609', 'Kono Subarashii Sekai ni Shukufuku wo!'),
    (3, 'Chris', 'Sample Description here', 'SSR','https://www.anime-planet.com/images/characters/thumbs/chris-72071.jpg?t=1453929795','Kono Subarashii Sekai ni Shukufuku wo!'),
    (4, 'Clemea', 'Sample Description here', 'R','https://www.anime-planet.com/images/characters/thumbs/clemea-101918.jpg?t=1485027334','Kono Subarashii Sekai ni Shukufuku wo!'),
    (5, 'Destroyer Creator', 'Sample Description here', 'N','https://www.anime-planet.com/images/characters/thumbs/destroyer-creator-103189.jpg?t=1585333987','Kono Subarashii Sekai ni Shukufuku wo!'),
    (6, 'Dust', 'Sample Description here', 'SR','https://www.anime-planet.com/images/characters/thumbs/dust-konosuba-gods-blessing-on-this-wonderful-world-102017.jpg?t=1459730946','Kono Subarashii Sekai ni Shukufuku wo!'),
    (7, 'Eris', 'Sample Description here', 'SSR','https://www.anime-planet.com/images/characters/thumbs/eris-kono-subarashii-sekai-ni-shukufuku-o-72077.jpg?t=1585335656','Kono Subarashii Sekai ni Shukufuku wo!'),
    (8, 'Fio', 'Sample Description here', 'SR','https://www.anime-planet.com/images/characters/thumbs/fio-konosuba-gods-blessing-on-this-wonderful-world-101917.jpg?t=1485027450','Kono Subarashii Sekai ni Shukufuku wo!'),
    (9, 'Galil', 'Sample Description here', 'N','https://www.anime-planet.com/images/characters/thumbs/galil-konosuba-gods-blessing-on-this-wonderful-world-100701.jpg?t=1456612478','Kono Subarashii Sekai ni Shukufuku wo!'),
    (10, 'Heinz', 'Sample Description here', 'N','https://www.anime-planet.com/images/characters/thumbs/heinz-konosuba-gods-blessing-on-this-wonderful-world-100700.jpg?t=1456612400','Kono Subarashii Sekai ni Shukufuku wo!'),
    (11, 'Keith', 'Sample Description here', 'N','https://www.anime-planet.com/images/characters/thumbs/keith-72076.jpg?t=1459730831','Kono Subarashii Sekai ni Shukufuku wo!'),
    (12, 'Kyouya Mitsurugi', 'Sample Description here', 'SSR','https://www.anime-planet.com/images/characters/thumbs/kyouya-mitsurugi-72086.jpg?t=1455225934','Kono Subarashii Sekai ni Shukufuku wo!'),
    (13, 'Luna', 'Sample Description here', 'SSR','https://www.anime-planet.com/images/characters/thumbs/luna-konosuba-gods-blessing-on-this-wonderful-world-100697.jpg?t=1456612243','Kono Subarashii Sekai ni Shukufuku wo!'),
    (14, 'Newbie Succubus', 'Sample Description here', 'SR','https://www.anime-planet.com/images/characters/thumbs/newbie-succubus-154173.jpg?t=1541519876','Kono Subarashii Sekai ni Shukufuku wo!'),
    (15, 'Priest', 'Sample Description here', 'N','https://www.anime-planet.com/images/characters/thumbs/priest-konosuba-gods-blessing-on-this-wonderful-world-101877.jpg?t=1457994886','Kono Subarashii Sekai ni Shukufuku wo!'),
    (16, 'Riin', 'Sample Description here', 'R','https://www.anime-planet.com/images/characters/thumbs/riin-konosuba-gods-blessing-on-this-wonderful-world-103187.jpg?t=1459732556','Kono Subarashii Sekai ni Shukufuku wo!'),
    (17, 'Ruffian', 'Sample Description here', 'SSR','https://www.anime-planet.com/images/characters/thumbs/ruffian-120119.jpg?t=1485033865','Kono Subarashii Sekai ni Shukufuku wo!'),
    (18, 'Sedol', 'Sample Description here', 'N','https://www.anime-planet.com/images/characters/thumbs/sedol-100699.jpg?t=1456612334','Kono Subarashii Sekai ni Shukufuku wo!'),
    (19, 'Sena', 'Sample Description here', 'SR','https://www.anime-planet.com/images/characters/thumbs/sena-konosuba-gods-blessing-on-this-wonderful-world-103188.jpg?t=1598780649','Kono Subarashii Sekai ni Shukufuku wo!'),
    (20, 'Taylor', 'Sample Description here', 'N','https://www.anime-planet.com/images/characters/thumbs/taylor-konosuba-gods-blessing-on-this-wonderful-world-103186.jpg?t=1459732434','Kono Subarashii Sekai ni Shukufuku wo!'),
    (21, 'Wiz', 'Sample Description here', 'SSR','https://www.anime-planet.com/images/characters/thumbs/wiz-72073.jpg?t=1466909441','Kono Subarashii Sekai ni Shukufuku wo!'),
    (22, 'Verdia', 'Sample Description here', 'SR','https://www.anime-planet.com/images/characters/thumbs/verdia-72083.jpg?t=1454545499','Kono Subarashii Sekai ni Shukufuku wo!'),
    (23, 'Darkness', 'Sample Description here', 'UR','https://www.anime-planet.com/images/characters/thumbs/darkness-konosuba-gods-blessing-on-this-wonderful-world-72068.jpg?t=1483863335','Kono Subarashii Sekai ni Shukufuku wo!'),
    (24, 'Megumin', 'Sample Description here', 'UR','https://www.anime-planet.com/images/characters/thumbs/megumin-72067.jpg?t=1542838491','Kono Subarashii Sekai ni Shukufuku wo!'),
    (25, 'Wolbach', 'Sample Description here', 'R','https://www.anime-planet.com/images/characters/thumbs/wolbach-72082.jpg?t=1489856108','Kono Subarashii Sekai ni Shukufuku wo! 2'),
    (26, 'Walther Alex Barnes', 'Sample Description here', 'R','https://www.anime-planet.com/images/characters/thumbs/walther-alex-barnes-72084.jpg?t=1486249142','Kono Subarashii Sekai ni Shukufuku wo! 2'),
    (27, 'Vanir', 'Sample Description here', 'SR','https://www.anime-planet.com/images/characters/thumbs/vanir-121195.jpg?t=1585331519','Kono Subarashii Sekai ni Shukufuku wo! 2'),
    (28, 'Previous King', 'Sample Description here', 'N','https://www.anime-planet.com/images/characters/thumbs/previous-king-120535.jpg?t=1485743860','Kono Subarashii Sekai ni Shukufuku wo! 2'),
    (29, 'Komekko', 'Sample Description here', 'SSR','https://www.anime-planet.com/images/characters/thumbs/komekko-141976.jpg?t=1585330990','Kono Subarashii Sekai ni Shukufuku wo! 2'),
    (30, 'Keele''s Love', 'Sample Description here', 'R','https://www.anime-planet.com/images/characters/thumbs/keeles-love-120536.jpg?t=1485744481','Kono Subarashii Sekai ni Shukufuku wo! 2'),
    (31, 'Keele', 'Sample Description here', 'SR','https://www.anime-planet.com/images/characters/thumbs/keele-120537.jpg?t=1485744603','Kono Subarashii Sekai ni Shukufuku wo! 2'),
    (32, 'Judge', 'Sample Description here', 'N','https://www.anime-planet.com/images/characters/thumbs/judge-konosuba-gods-blessing-on-this-wonderful-world-120112.jpg?t=1485028043','Kono Subarashii Sekai ni Shukufuku wo! 2'),
    (33, 'Jarippa', 'Sample Description here', 'N','https://www.anime-planet.com/images/characters/thumbs/jarippa-121622.jpg?t=1488738187','Kono Subarashii Sekai ni Shukufuku wo! 2'),
    (34, 'Ignis Dustiness Ford', 'Sample Description here', 'R','https://www.anime-planet.com/images/characters/thumbs/ignis-dustiness-ford-120866.jpg?t=1486247416','Kono Subarashii Sekai ni Shukufuku wo! 2'),
    (35, 'Hot Springs Manager', 'Sample Description here', 'N','https://www.anime-planet.com/images/characters/thumbs/hot-springs-manager-122296.jpg?t=1489853878','Kono Subarashii Sekai ni Shukufuku wo! 2'),
    (36, 'Hans', 'Sample Description here', 'R','https://www.anime-planet.com/images/characters/thumbs/hans-konosuba-gods-blessing-on-this-wonderful-world-2-72070.jpg?t=1489854167','Kono Subarashii Sekai ni Shukufuku wo! 2'),
    (37, 'Chomusuke', 'Sample Description here', 'SR','https://www.anime-planet.com/images/characters/thumbs/chomusuke-120030.jpg?t=1484789398','Kono Subarashii Sekai ni Shukufuku wo! 2'),
    (38, 'Aldarp Alex Barnes', 'Sample Description here', 'R','https://www.anime-planet.com/images/characters/thumbs/aldarp-alex-barnes-119837.jpg?t=1484409379','Kono Subarashii Sekai ni Shukufuku wo! 2'),
    (39, 'Yunyun', 'Sample Description here', 'SSR','https://www.anime-planet.com/images/characters/thumbs/yunyun-72080.jpg?t=1466909539','Kono Subarashii Sekai ni Shukufuku wo! 2'),
    (40, 'Wagon Driver', 'Sample Description here', 'N', 'https://www.anime-planet.com/images/characters/thumbs/wagon-driver-121621.jpg?t=1488737842', 'Kono Subarashii Sekai ni Shukufuku wo! 2'),
    (41, 'Kazuma', 'Sample Description here', 'UR', 'https://www.anime-planet.com/images/characters/thumbs/kazuma-satou-72069.jpg?t=1453327584', 'Kono Subarashii Sekai ni Shukufuku wo!')
    (42, 'Mordred', 'Sample Description here', 'UR', 'https://i.imgur.com/s8Cn7QH.png', 'Fate/Apocrypha'),
    (43, 'Tatsuya Shiba', 'Sample Descr', 'UR','https://www.anime-planet.com/images/characters/thumbs/tatsuya-shiba-55173.jpg?t=1585114950', 'Mahouka Koukou no Rettousei'),
    (44, 'Tatsumaki', 'Sample Descr', 'UR','https://www.anime-planet.com/images/characters/tornado-of-terror-91110.jpg?t=1454274128', 'One-Punch Man'),
    (45, 'Monkey D. Luffy', 'Sample Description', 'UR', 'https://www.anime-planet.com/images/characters/thumbs/monkey-d-luffy-74.jpg?t=1549566613', 'One Piece'),
    (46, 'Roronoa Zoro', 'Sample Description', 'UR', 'https://www.anime-planet.com/images/characters/thumbs/zoro-roronoa-75.jpg?t=1551804980', 'One Piece'),
    (47, 'Nami', 'Sample Description', 'UR', 'https://www.anime-planet.com/images/characters/thumbs/nami-76.jpg?t=1544025770', 'One Piece'),
    (48, 'Usopp', 'Sample Description', 'UR', 'https://www.anime-planet.com/images/characters/thumbs/usopp-77.jpg?t=1429318036', 'One Piece'),
    (49, 'Sanji', 'Sample Description', 'UR', 'https://www.anime-planet.com/images/characters/thumbs/sanji-78.jpg?t=1549471772', 'One Piece'),
    (50, 'Chopper', 'Sample Description', 'UR', 'https://www.anime-planet.com/images/characters/thumbs/robin-nico-80.jpg?t=1429317927', 'One Piece'),
    (51, 'Robin', 'Sample Description', 'UR', 'https://www.anime-planet.com/images/characters/thumbs/tony-tony-chopper-79.jpg?t=1546521587', 'One Piece'),
    (52, 'Franky', 'Sample Description', 'UR', 'https://www.anime-planet.com/images/characters/thumbs/franky-flam-81.jpg?t=1496845412', 'One Piece'),
    (53, 'Brook', 'Sample Description', 'UR', 'https://www.anime-planet.com/images/characters/thumbs/brook-82.jpg?t=1554330822', 'One Piece'),
    (54, 'Portgas D. Ace', 'Sample Description', 'UR', 'https://www.anime-planet.com/images/characters/thumbs/ace-d-portgas-291.jpg?t=1535065324', 'One Piece'),
    (55, 'Shanks', 'Sample Description', 'UR', 'https://www.anime-planet.com/images/characters/thumbs/shanks-968.jpg?t=1543019705', 'One Piece'),
    (56, 'Dracule Mihawk', 'Sample Description', 'UR', 'https://www.anime-planet.com/images/characters/thumbs/juracule-mihawk-972.jpg?t=1543167492', 'One Piece'),
    (57, 'Arlong', 'Sample Description', 'SSR', 'https://www.anime-planet.com/images/characters/thumbs/arlong-294.jpg?t=1544024961', 'One Piece'),
    (58, 'Fat Alvida', 'Sample Description', 'SR', 'https://www.anime-planet.com/images/characters/thumbs/alvida-1001.jpg?t=1543167158', 'One Piece'),
    (59, 'Axe Hand Morgan', 'Sample Description', 'SR', 'https://www.anime-planet.com/images/characters/thumbs/jinbei-1676.jpg?t=1429317730', 'One Piece'),
    (60, 'Coby', 'Sample Description', 'SSR', 'https://www.anime-planet.com/images/characters/thumbs/coby-1041.jpg?t=1544700189', 'One Piece'),
    (61, 'Helmeppo', 'Sample Description', 'SR', 'https://www.anime-planet.com/images/characters/thumbs/helmeppo-1042.jpg?t=1543167620', 'One Piece'),
    (62, 'Gaimon', 'Sample Description', 'SR', 'https://www.anime-planet.com/images/characters/thumbs/gaimon-1012.jpg?t=1543511417', 'One Piece'),
    (63, 'Higuma', 'Sample Description', 'N', 'https://www.anime-planet.com/images/characters/thumbs/higuma-13285.jpg?t=1543167790', 'One Piece'),
    (64, 'Lord of the Coast', 'Sample Description', 'N', 'https://static.wikia.nocookie.net/onepiece/images/b/b2/Lord_of_the_Coast_Portrait.png/revision/latest/scale-to-width-down/119?cb=20200112093708', 'One Piece'),
    (65, 'Rika', 'Sample Description', 'N', 'https://static.wikia.nocookie.net/onepiece/images/8/89/Rika_Portrait.png/revision/latest/scale-to-width-down/119?cb=20200112100117', 'One Piece'),
    (66, 'Ririka', 'Sample Description', 'N', 'https://static.wikia.nocookie.net/onepiece/images/3/32/Ririka_Portrait.png/revision/latest/scale-to-width-down/119?cb=20200112095840', 'One Piece'),
    (67, 'Ukkari', 'Sample Description', 'N', 'https://static.wikia.nocookie.net/onepiece/images/9/97/Ukkari_Portrait.png/revision/latest/scale-to-width-down/119?cb=20200112100636', 'One Piece'),
    (68, 'Rokkaku', 'Sample Description', 'N', 'https://static.wikia.nocookie.net/onepiece/images/4/4f/Rokkaku_Portrait.png/revision/latest/scale-to-width-down/119?cb=20200112100313', 'One Piece'),
    (69, 'Ripper', 'Sample Description', 'N', 'https://static.wikia.nocookie.net/onepiece/images/4/46/Ripper_Portrait.png/revision/latest/scale-to-width-down/119?cb=20200112100518', 'One Piece'),
    (70, 'Koshirou', 'Sample Description', 'N', 'https://www.anime-planet.com/images/characters/thumbs/koshiro-13291.jpg?t=1544025425', 'One Piece'),
    (71, 'Kuina', 'Sample Description', 'SR', 'https://www.anime-planet.com/images/characters/thumbs/kuina-1309.jpg?t=1543964079', 'One Piece'),
    (72, 'Boodle', 'Sample Description', 'N', 'https://www.anime-planet.com/images/characters/thumbs/boodle-13292.jpg?t=1543498383', 'One Piece'),
    (73, 'Chouchou', 'Sample Description', 'R', 'https://static.wikia.nocookie.net/onepiece/images/5/52/Chouchou_Portrait.png/revision/latest/scale-to-width-down/119?cb=20200105082049', 'One Piece'),
    (74, 'Poro', 'Sample Description', 'N', 'https://www.anime-planet.com/images/characters/thumbs/poro-83793.jpg?t=1543502085', 'One Piece'),
    (75, 'Kaya', 'Sample Description', 'R', 'https://www.anime-planet.com/images/characters/thumbs/kaya-978.jpg?t=1429317755', 'One Piece'),
    (76, 'Merry', 'Sample Description', 'N', 'https://www.anime-planet.com/images/characters/thumbs/merry-13294.jpg?t=1543511539', 'One Piece'),
    (77, 'Banchina', 'Sample Description', 'N', 'https://www.anime-planet.com/images/characters/thumbs/banchina-83656.jpg?t=1532109553', 'One Piece'),
    (78, 'Ninjin', 'Sample Description', 'N', 'https://www.anime-planet.com/images/characters/thumbs/ninjin-981.jpg?t=1543168673', 'One Piece'),
    (79, 'Tamanegi', 'Sample Description', 'N', 'https://www.anime-planet.com/images/characters/thumbs/tamanegi-979.jpg?t=1543169394', 'One Piece'),
    (80, 'Piman', 'Sample Description', 'N', 'https://www.anime-planet.com/images/characters/thumbs/piman-980.jpg?t=1543168874', 'One Piece'),
    (81, 'Captain Kuro', 'Sample Description', 'SSR', 'https://www.anime-planet.com/images/characters/thumbs/kuro-949.jpg?t=1543168066', 'One Piece'),
    (82, 'Zeff', 'Sample Description', 'SR', 'https://www.anime-planet.com/images/characters/thumbs/zeff-995.jpg?t=1543169805', 'One Piece'),
    (83, 'Patty', 'Sample Description', 'N', 'https://www.anime-planet.com/images/characters/thumbs/patty-996.jpg?t=1543964282', 'One Piece'),
    (84, 'Carne', 'Sample Description', 'N', 'https://www.anime-planet.com/images/characters/thumbs/carne-one-piece-14552.jpg?t=1543963747', 'One Piece'),
    (85, 'Buggy', 'Sample Description', 'SSR', 'https://www.anime-planet.com/images/characters/thumbs/buggy-83.jpg?t=1543498435', 'One Piece'),
    (86, 'Bellemere', 'Sample Description', 'R', 'https://www.anime-planet.com/images/characters/thumbs/bellemere-992.jpg?t=1544025018', 'One Piece'),
    (87, 'Nojiko', 'Sample Description', 'SR', 'https://www.anime-planet.com/images/characters/thumbs/nojiko-994.jpg?t=1544025829', 'One Piece'),
    (88, 'Genzo', 'Sample Description', 'N', 'https://www.anime-planet.com/images/characters/thumbs/genzo-993.jpg?t=1544025170', 'One Piece'),
    (89, 'Nako', 'Sample Description', 'N', 'https://www.anime-planet.com/images/characters/thumbs/nako-14557.jpg?t=1544025603', 'One Piece'),
    (90, 'Johnny', 'Sample Description', 'R', 'https://www.anime-planet.com/images/characters/thumbs/johnny-1311.jpg?t=1543963949', 'One Piece'),
    (91, 'Yosaku', 'Sample Description', 'R', 'https://www.anime-planet.com/images/characters/thumbs/yosaku-1312.jpg?t=1543964407', 'One Piece'),
    (92, 'Heppoko', 'Sample Description', 'N', 'https://www.anime-planet.com/images/characters/thumbs/heppoko-83698.jpg?t=1543167689', 'One Piece'),
    (93, 'Peppoko', 'Sample Description', 'N', 'https://www.anime-planet.com/images/characters/thumbs/peppoko-83788.jpg?t=1543168782', 'One Piece'),
    (94, 'Poppoko', 'Sample Description', 'N', 'https://www.anime-planet.com/images/characters/thumbs/poppoko-83792.jpg?t=1543168989', 'One Piece'),
    (95, 'Mohji', 'Sample Description', 'N', 'https://www.anime-planet.com/images/characters/thumbs/mohji-1136.jpg?t=1543498733', 'One Piece'),
    (96, 'Cabaji', 'Sample Description', 'N', 'https://www.anime-planet.com/images/characters/thumbs/cabaji-1135.jpg?t=1543498506', 'One Piece'),
    (97, 'Richie', 'Sample Description', 'R', 'https://www.anime-planet.com/images/characters/thumbs/richie-1137.jpg?t=1555508757', 'One Piece'),
    (98, 'Sham', 'Sample Description', 'N', 'https://static.wikia.nocookie.net/onepiece/images/5/55/Sham_Portrait.png/revision/latest/scale-to-width-down/119?cb=20181213040534', 'One Piece'),
    (99, 'Don Krieg', 'Sample Description', 'SSR', 'https://static.wikia.nocookie.net/onepiece/images/0/0a/Buchi_Portrait.png/revision/latest/scale-to-width-down/119?cb=20200112123533', 'One Piece'),
    (100, 'Snakeman Luffy', 'Sample Description', 'UR', 'https://static.wikia.nocookie.net/onepiece/images/a/ab/Snakeman.png/revision/latest/scale-to-width-down/340?cb=20190202171603', 'One Piece'),
    (101, 'Gin', 'Sample Description', 'R', 'https://www.anime-planet.com/images/characters/thumbs/gin-one-piece-1316.jpg?t=1543167550', 'One Piece'),
    (102, 'Pearl', 'Sample Description', 'N', 'https://www.anime-planet.com/images/characters/thumbs/pearl-one-piece-13341.jpg?t=1543964352', 'One Piece'),
    (103, 'Chew', 'Sample Description', 'R', 'https://www.anime-planet.com/images/characters/thumbs/chew-1007.jpg?t=1544025115', 'One Piece'),
    (104, 'Kuroobi', 'Sample Description', 'R', 'https://www.anime-planet.com/images/characters/thumbs/kuroobi-1008.jpg?t=1544025492', 'One Piece'),
    (105, 'Hatchan', 'Sample Description', 'SR', 'https://www.anime-planet.com/images/characters/thumbs/hatchan-295.jpg?t=1544017739', 'One Piece'),
    (106, 'Momoo', 'Sample Description', 'N', 'https://www.anime-planet.com/images/characters/thumbs/momoo-13343.jpg?t=1544025543', 'One Piece');
