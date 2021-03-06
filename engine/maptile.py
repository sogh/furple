from enum import Enum


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
        self.local_npcs = []

    def toString(self):
        return self.name + "\n" + self.description

    def add_item(self, new_item):
        self.local_items.append(new_item)

    def reveal_items(self):
        return [thing.description for thing in self.local_items]

    def add_npc(self, new_npc):
        self.local_npcs.append(new_npc)
    
    def reveal_npcs(self):
        return [npc.recall_name() for npc in self.local_npcs]
    
    def greet_npcs(self):
        return [npc.greet() for npc in self.local_npcs]

    def pickup_item(self, description):
        item_index = 0
        for item in self.local_items:
            if item.description == description:
                return self.local_items.pop(item_index)
            item_index += 1
        return None
