import unittest
from engine.maptile import MapTile, MapTileTag
from engine.npc import NPC
from engine.detritus import Detritus

class MapTileTest(unittest.TestCase):
    
    def setUp(self):
        self.test_detritus = Detritus('A rock')
        self.test_npc = NPC(0,0)
        self.test_cave_tile = MapTile('cave_tile', 'cavey cave', [MapTileTag.CAVE])
        self.test_cave_tile.add_item(self.test_detritus)
        self.test_cave_tile.add_npc(self.test_npc)

    def testToString(self):
        self.assertEqual(self.test_cave_tile.toString(), self.test_cave_tile.name + "\n" + self.test_cave_tile.description)

    def testItems(self):
        self.assertEqual([self.test_detritus.description], self.test_cave_tile.reveal_items())
        self.assertEqual(self.test_detritus, self.test_cave_tile.pickupitem("A rock"))
        self.assertEqual("You cannot get that.", self.test_cave_tile.pickupitem("A rock"))

    def testNPC(self):
        self.assertEqual([self.test_npc.recall_name()], self.test_cave_tile.reveal_npcs())
        self.assertEqual([self.test_npc.greet()], self.test_cave_tile.greet_npcs())

if __name__ == '__main__':
    unittest.main()
