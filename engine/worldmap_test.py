import unittest
from engine.worldmap import WorldMap
from engine.detritus import Detritus
from engine.maptile import MapTile, MapTileTag

class WorldMapTest(unittest.TestCase):

    def setUp(self):
        self.test_detritus_description = "hunk o junk"
        self.test_detritus = Detritus(self.test_detritus_description, [self.test_detritus_description], True)
        self.test_tile = MapTile("testforest", "a test forest", MapTileTag.FOREST)
        self.test_worldmap = WorldMap(-3, -3, 3, 3)
        self.test_worldmap.AddItemAt(1, 0, self.test_detritus)
        self.test_worldmap.SetMapTile(0, 0, self.test_tile)
        self.test_worldmap.AddNPCAt(1, 1, 'testnpcname')

    def testLocationDescription(self):
        self.assertEqual(self.test_tile.toString(), self.test_worldmap.GetLocationDescription(0,0))

    def testItemDescription(self):
        self.assertEqual([self.test_detritus_description], self.test_worldmap.GetItemDescriptions(1,0))
    
    def testNPCs(self):
        self.assertGreater(len(self.test_worldmap.GetNPCDescriptions(1,1)), 0)
        self.assertGreater(len(self.test_worldmap.greetnpcs(1,1)), 0)

    def test_retrieve_item(self):
        self.assertEqual(self.test_worldmap.pickup_items(1,0,self.test_detritus_description).description, self.test_detritus_description)
        self.assertEqual(self.test_worldmap.pickup_items(1,0,self.test_detritus_description), None) 


if __name__ == '__main__':
    unittest.main()