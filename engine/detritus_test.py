import unittest

from engine.detritus import Detritus

class DetritusTestCase(unittest.TestCase):
    """Tests for items."""

    def setUp(self):
        """Create items for use in testing."""
        self.item1 = Detritus('stick')

    def test_description(self):
        """Test item description."""
        self.assertEqual(self.item1.description, 'stick')
        self.assertNotEqual(self.item1.description, 'ball')

if __name__ == '__main__':
    unittest.main()