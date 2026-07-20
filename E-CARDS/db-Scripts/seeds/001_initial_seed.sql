-- Seed collections
INSERT INTO tbl_collections (collectionSetName, releaseDate, totalCardsInCollection)
VALUES
('Base Set', '1999-01-09', 102),
('Jungle', '1999-06-16', 64),
('Fossil', '1999-10-10', 62);

-- Seed types
INSERT INTO tbl_types (typeName)
VALUES
('Grass'),
('Fire'),
('Water'),
('Lightning'),
('Psychic'),
('Fighting'),
('Colorless');

-- Seed stages
INSERT INTO tbl_stages (stageName)
VALUES
('Basic'),
('Stage 1'),
('Stage 2');

-- Seed cards
INSERT INTO tbl_cards (hp, name, info, attack, damage, weak, resis, retreat,
                       cardNumberInCollection, collection_id, type_id, stage_id)
VALUES
(60, 'Bulbasaur', 'Seed Pokémon', 'Vine Whip', '20', 'Fire', 'Water', '1',
 1, 1, 1, 1),

(50, 'Charmander', 'Lizard Pokémon', 'Ember', '30', 'Water', 'Grass', '1',
 4, 1, 2, 1),

(50, 'Squirtle', 'Tiny Turtle Pokémon', 'Bubble', '20', 'Lightning', 'Fire', '1',
 7, 1, 3, 1),

(40, 'Pikachu', 'Mouse Pokémon', 'Thunder Jolt', '30', 'Fighting', 'Steel', '1',
 25, 1, 4, 1),

(60, 'Jigglypuff', 'Balloon Pokémon', 'Pound', '20', 'Fighting', 'Psychic', '1',
 54, 1, 7, 1),

(90, 'Scyther', 'Mantis Pokémon', 'Slash', '30', 'Fire', 'Fighting', '1',
 10, 2, 1, 1),

(100, 'Hitmonlee', 'Kicking Pokémon', 'Stretch Kick', '50', 'Psychic', 'None', '2',
 7, 3, 6, 1);
