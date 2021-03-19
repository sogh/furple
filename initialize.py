"""This module initializes map, items, and npcs."""
from random import randint, choice
from engine.worldmap import WorldMap
from engine.maptile import MapTile
from engine.maptile import MapTileTag
from engine.detritus import Detritus

def GENERATE_PHEZYGG_WORLD():
    phezygg_world = WorldMap(-25, -25, 25, 25)
    phezygg_world.SetMapTile(0, 0, MapTile('start', 'Its the start.'))
    phezygg_world.SetMapTile(0, 1,
        MapTile('pforest', 
                'Its a forest of penises, you need to get out of here, '
                'if only you could stop tripping ass-first.',
                [MapTileTag.FOREST]))
    phezygg_world.SetMapTile(1, 1,
        MapTile('forest', 
                'Its a forest, you could see it better if not for all these damn trees.',
                [MapTileTag.FOREST]))
    phezygg_world.SetMapTile(-1, 1,
        MapTile('mforest', 
                'Its a forest of mushrooms.',
                [MapTileTag.FOREST]))
    phezygg_world.SetMapTile(1, 0,
        MapTile('market', 
                'An ancient market destroyed by nuclear fire, the diminutive shadows on the wall bring a tear to your eye.',
                [MapTileTag.MARKET]))
    phezygg_world.SetMapTile(-1, 0,
        MapTile('cave', 
                'A deep cave.',
                [MapTileTag.CAVE]))
    phezygg_world.SetMapTile(0, -1,
        MapTile('dessert', 
                'An endless dessert, it looks delicious.',
                [MapTileTag.DESSERT]))
    phezygg_world.SetMapTile(1, -1,
        MapTile('desert', 
                'Its a desert, the cake turns to sand in your mouth.',
                [MapTileTag.DESERT]))
    phezygg_world.SetMapTile(-1, -1,
        MapTile('dessertdesert', 
                'There seems to be nothing here.',
                [MapTileTag.DESSERT, MapTileTag.DESERT]))
    initial_item_populate(phezygg_world)
    initial_npc_populate(phezygg_world)
    return phezygg_world

def initial_item_populate(new_world, north_limit = 1, south_limit = -1, east_limit = 1, west_limit = -1):
    possible_items = [
        {
            'description': 'a rock',
            'synonyms': ['a rock', 'rock', 'the rock'],
            'obtainable': True,
        },
        {
            'description': 'a tree',
            'synonyms': ['a tree', 'tree', 'the tree'],
            'obtainable': False,
        },
        {
            'description': 'a stream',
            'synonyms': ['a stream', 'stream', 'the stream'],
            'obtainable': False,
        },
        {
            'description': 'a boot',
            'synonyms': ['a boot', 'boot', 'the boot'],
            'obtainable': True,
        },
        {
            'description': 'some grass',
            'synonyms': ['some grass', 'grass', 'the grass'],
            'obtainable': False,
        },
        {
            'description': 'some mushrooms',
            'synonyms': ['some mushrooms', 'mushrooms', 'the mushrooms'],
            'obtainable': True,
        },
        {
            'description': 'a cloud',
            'synonyms': ['a cloud', 'cloud', 'the cloud'],
            'obtainable': False,
        },
        {
            'description': 'crumpled paper',
            'synonyms': ['crumpled paper', 'paper', 'the paper', 'the crumpled paper'],
            'obtainable': True,
        },
        {
            'description': 'a fallen tree limb',
            'synonyms': ['a fallen tree limb', 'fallen tree limb', 'the fallen tree limb', 'tree limb', 'a tree limb', 'the tree limb'],
            'obtainable': False,
        },
    ]
    max_initial_items = 7

    for _ in range(randint(1,max_initial_items)):
        new_item = choice(possible_items)
        new_world.AddItemAt(choice(list(range(west_limit, east_limit + 1))), choice(list(range(south_limit, north_limit + 1))), Detritus(description=new_item['description'], synonyms=new_item['synonyms'], obtainable=new_item['obtainable']))

    new_world.AddItemAt(0,0, Detritus('a key', ['key', 'a key', 'the key'], True))
    new_world.AddItemAt(1, 0, Detritus('a door', ['door', 'a door', 'the door'], False))

def initial_npc_populate(new_world, north_limit = 1, south_limit = -1, east_limit = 1, west_limit = -1):
    max_initial_npc = 4
    possible_names = ['steve', 'mark', 'jill', 'edna']

    for _ in range(randint(1,max_initial_npc)):
        npc_name = choice(possible_names)
        possible_names.remove(npc_name)
        new_world.AddNPCAt(choice(list(range(west_limit, east_limit + 1))), choice(list(range(south_limit, north_limit + 1))), npc_name)