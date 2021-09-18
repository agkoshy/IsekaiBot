create table Player (
    discord_id  bigint not null,
    gold        bigint not null,
    adv         timestamp,
    plvl        int    not null,
    pexp        int    not null,
    strh        bigint not null,
    dex         bigint not null,
    intl        bigint not null,
    boss        varchar(300),
    title       varchar(300),
    game_state  varchar(300),    
    constraint User_PK
        primary key(discord_id)
);