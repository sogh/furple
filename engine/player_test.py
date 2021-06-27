import unittest

from engine.player import Player, HUNGER_PHASE_DURATION
from engine.detritus import Detritus

class PlayerTestCase(unittest.TestCase):
    """Tests Player class and functions."""

    def setUp(self):
        """Create a Player for use in testing."""
        self.player1 = Player()
        self.testitem = Detritus("A ROCK")

    def test_move(self):
        """Test player position and movement."""
        # Check default x position
        self.assertEqual(self.player1.position.x, 0)
        # Check default y position
        self.assertEqual(self.player1.position.y, 0)
        # Check the different move directions and the resulting position change
        self.player1.move('n')
        self.assertEqual(self.player1.position.y, 1)
        self.player1.move('s')
        self.assertEqual(self.player1.position.y, 0)
        self.player1.move('e')
        self.assertEqual(self.player1.position.x, 1)
        self.player1.move('w')
        self.assertEqual(self.player1.position.x, 0)

    def test_status(self):
        """Test player hunger level and update."""
        # Check initial hunger
        self.assertEqual(self.player1.PlayerStatus(), 'You feel content.')
        self.assertEqual(self.player1.hunger, 0)
        for i in range(0,4):
            self.player1.Update((i + 1) * HUNGER_PHASE_DURATION)
        self.assertEqual(self.player1.hunger, 4)
        self.assertEqual(self.player1.PlayerStatus(), 'You are hungry.')

    def test_inventory(self):
        """Test inventory."""
        self.player1.add_item_to_inv(self.testitem)
        self.assertIn(self.testitem, self.player1.inventory)
        self.assertEqual(self.player1.display_inv(),["A ROCK"])



if __name__ == '__main__':
    unittest.main()