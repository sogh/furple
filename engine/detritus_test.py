import unittest

from engine.detritus import Detritus

class DetritusTestCase(unittest.TestCase):
    """Tests for items."""

    def setUp(self):
        """Create items for use in testing."""
        self.item1 = Detritus('stick', ['stick', 'branch'], True)

    def test_description(self):
        """Test item description."""
        self.assertEqual(self.item1.get_description(), 'stick')
        self.assertNotEqual(self.item1.get_description(), 'ball')

    def test_synonyms(self):
        """Test item synonym list."""
        self.assertEqual(['stick', 'branch'], self.item1.get_synonyms())

    def test_obtainable(self):
        """Test item obtainable property."""
        self.assertEqual(self.item1.is_obtainable(), True)

if __name__ == '__main__':
    unittest.main()