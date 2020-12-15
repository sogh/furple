"""This module initializes map, items, and npcs."""
from random import randint, choice
from engine.worldmap import WorldMap
from engine.worldmap import MapTile
from engine.worldmap import MapTileTag

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
    return phezygg_world

def initial_item_populate(new_world, north_limit = 1, south_limit = -1, east_limit = 1, west_limit = -1):
    possible_items = ['a tree', 'a rock', 'a stream', 'a boot', 'some grass', 'some mushrooms', 'a cloud', 'crumpled paper', 'a fallen tree limb']
    max_initial_items = 7

    for _ in range(randint(1,max_initial_items)):
        new_world.AddItemAt(choice(list(range(west_limit, east_limit + 1))), choice(list(range(south_limit, north_limit + 1))), choice(possible_items))

def initial_npc_populate(new_world, north_limit = 1, south_limit = -1, east_limit = 1, west_limit = -1):
    max_initial_npc = 4

    for _ in range(randint(1,max_initial_npc)):
        new_world.AddNPCAt(choice(list(range(west_limit, east_limit + 1))), choice(list(range(south_limit, north_limit + 1))))