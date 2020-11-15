from engine.worldmap import WorldMap
from engine.worldmap import MapTile
from engine.worldmap import MapTileTag

def GENERATE_PHEZYGG_WORLD():
    phezygg_world = WorldMap(-25, -25, 25, 25)
    phezygg_world.SetMapTile(0, 0, MapTile('start', 'Its the start.'))
    phezygg_world.SetMapTile(0, 1,
        MapTile('pforest', 
                '''Its a forest of penises, you need to get out of here,
                if only you could stop tripping ass-first.''',
                [MapTileTag.FOREST]))
    phezygg_world.SetMapTile(1, 1,
        MapTile('forest', 
                '''Its a forest, you could see it better if not for all these damn trees.''',
                [MapTileTag.FOREST]))
    phezygg_world.SetMapTile(-1, 1,
        MapTile('mforest', 
                '''Its a forest of mushrooms.''',
                [MapTileTag.FOREST]))
    phezygg_world.SetMapTile(1, 0,
        MapTile('market', 
                '''An ancient market destroyed by nuclear fire, the diminutive shadows on the wall bring a tear to your eye.''',
                [MapTileTag.MARKET]))
    phezygg_world.SetMapTile(-1, 0,
        MapTile('cave', 
                '''A deep cave.''',
                [MapTileTag.CAVE]))
    phezygg_world.SetMapTile(0, -1,
        MapTile('dessert', 
                '''An endless dessert, it looks delicious.''',
                [MapTileTag.DESSERT]))
    phezygg_world.SetMapTile(1, -1,
        MapTile('desert', 
                '''Its a desert, the cake turns to sand in your mouth.''',
                [MapTileTag.DESERT]))
    phezygg_world.SetMapTile(-1, -1,
        MapTile('dessertdesert', 
                '''There seems to be nothing here.''',
                [MapTileTag.DESSERT, MapTileTag.DESERT]))
    return phezygg_world
