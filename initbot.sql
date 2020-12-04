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

insert into Gear (gear_id, gear, descr, equiptype, rarity, gold) values
    (1, 'Goblin Slayer Helm', 'The helmet of an expert in slaying goblins', 'Helmet', 'D', 50),
    (2, 'Bloodied Shortsword', 'The shortsword of a dead adventure', 'Weapon', 'F', 1),
    (3, 'Leather Chest', 'A flexible chest made out of monster leather', 'Chest', 'E', 3),
    (4, 'Torch', 'An item to light the way', 'Weapon', 'F', 1);

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