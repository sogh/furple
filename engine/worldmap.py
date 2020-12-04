from enum import Enum
from engine.detritus import Detritus

class MapTileTag(Enum):
    PLAINS = 0
    DESERT = 1
    DESSERT = 2
    FOREST = 3
    MOUNTAIN = 4
    FOGGY = 5
    CAVE = 6
    WATER = 7
    MARKET = 8


class MapTile:
    def __init__(self, name = "Unnamed", description = "An empty place.", taglist = []):
        self.tags = taglist
        self.name = name
        self.description = description
        self.local_items = []

    def toString(self):
        return self.name + "\n" + self.description

    def add_item(self, new_item):
        self.local_items.append(new_item)

    def reveal_items(self):
        return [thing.description for thing in self.local_items]

    


class WorldMap:
    """ Constructor takes starting and ending coordinates to generate an initial map."""
    def __init__(self, start_x, start_y, end_x, end_y):
        # Dict comprehension that builds the initial dict of dicts that is our world map
        # Similar to:
        # for x in range(start_x, end_x):
        #     for y in range(start_y, end_y):
        #         self.map[x][y] = MapTile()
        # but in one line
        self.map = {x:{y: MapTile() for y in range(start_y, end_y)} for x in range(start_x, end_x)}

    def SetMapTile(self, x, y, tile):
        self.map[x][y] = tile

    def GetLocationDescription(self, x, y):
        return self.map[x][y].toString()

    def AddItemAt(self, x, y, item_description):
        self.map[x][y].add_item(Detritus(item_description.lower()))
    
    def GetItemDescriptions(self, x, y):
        return self.map[x][y].reveal_items()