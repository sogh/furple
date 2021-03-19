from engine.maptile import MapTile
from engine.detritus import Detritus
from engine.npc import NPC


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

    def AddItemAt(self, x, y, item):
        self.map[x][y].add_item(item)
    
    def GetItemDescriptions(self, x, y):
        return self.map[x][y].reveal_items()

    def AddNPCAt(self, x, y, npc_name):
        self.map[x][y].add_npc(NPC(x, y, npc_name))

    def GetNPCDescriptions(self, x, y):
        return self.map[x][y].reveal_npcs()

    def greetnpcs(self, x, y):
        return self.map[x][y].greet_npcs()
    
    def pickup_items(self, x, y, description):
        return self.map[x][y].pickup_item(description)