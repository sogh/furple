import unittest

from engine.npc import NPC

class NPCTestCase(unittest.TestCase):
    """Tests NPC class functions."""

    def setUp(self):
        """Creates an NPC for use in testing."""
        self.test_npc_name = 'david'
        self.test_npc = NPC(1, -1, self.test_npc_name)

    def test_name(self):
        """Test NPC name."""
        self.assertEqual(self.test_npc.recall_name(), self.test_npc_name)
        self.assertNotEqual(self.test_npc.recall_name(), 'bob')

    def test_greeting(self):
        """Test NPC greeting function."""
        self.assertEqual(self.test_npc.greet(), f"{self.test_npc_name.title()}:  Hi!, my name is {self.test_npc_name.title()}!")

    def test_npc_position(self):
        """Test NPC positioning."""
        self.assertEqual(self.test_npc.position.x, 1)

if __name__ == '__main__':
    unittest.main()