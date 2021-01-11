import unittest
from point import Point

class PointTest(unittest.TestCase):
    def testX(self):
        p = Point(3, 7)
        self.assertEqual(p.x, 3)
        self.assertEqual(p.y, 7)
        p.x = 99
        self.assertEqual(p.x, 99)
        p.y = -45
        self.assertEqual(p.y, -45)


if __name__ == '__main__':
    unittest.main()