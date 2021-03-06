import unittest
from mygame import MyGame
from engine.player  import Player
from engine.simulation import Simulation
from engine.graphics import Graphics
from engine.sunmoon import SunMoon
from engine.worldmap import WorldMap
from engine.maptile import MapTile, MapTileTag


class MyGameTest(unittest.TestCase):
    def setUp(self):
        # Here we will construct a Test World we can use to verify our systems
        # work well together.
        self.player = Player()        
        self.g = Graphics()
        self.sim = Simulation()
        self.sun = SunMoon()

        # Build Test World
        self.worldmap = WorldMap(0, 0, 2, 2)
        self.worldmap.SetMapTile(0, 0, MapTile('00', 'ohoh', [MapTileTag.FOREST]))
        self.worldmap.SetMapTile(0, 1, MapTile('01', 'oh one', [MapTileTag.FOREST]))
        self.worldmap.SetMapTile(1, 0, MapTile('10', 'ten', [MapTileTag.FOREST]))
        self.worldmap.SetMapTile(1, 1, MapTile('11', 'eleven', [MapTileTag.FOREST]))

        self.worldmap.AddItemAt(0, 1, 'Test Item')

        # Create Test NPC
        self.worldmap.AddNPCAt(1, 0, 'roger')
        self.worldmap.AddNPCAt(1, 0, 'bob')

        self.game = MyGame(worldmap=self.worldmap,sim=self.sim,
            player1=self.player,graphics=self.g, sun=self.sun)
    
    def test_PlayerCanMove(self):
        # Player starts at 0,0
        self.assertEqual(self.player.position.x, 0)
        self.assertEqual(self.player.position.y, 0)
        # Simulate input command 'e'
        self.game.input_queue.append('e')
        # Move the game forward one step
        self.game.Step()
        # Verify player moved
        self.assertEqual(self.player.position.x, 1)
        self.assertEqual(self.player.position.y, 0)

    def test_NPCTests(self):
        """Tests for NPC Class."""
        self.assertIn('roger', self.worldmap.GetNPCDescriptions(1,0))
        self.assertIn('bob', self.worldmap.GetNPCDescriptions(1,0))

if __name__ == '__main__':
    unittest.main()