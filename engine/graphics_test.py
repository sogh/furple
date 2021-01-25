import unittest
from engine.graphics import Graphics

class GraphicsTest(unittest.TestCase):
    def setUp(self):
        self.graphics = Graphics()

    def testRenderText(self):
        self.assertEqual(len(self.graphics.render_list), 0)
        self.graphics.RenderText('Poop')
        self.assertEqual(len(self.graphics.render_list), 1)
        self.graphics.Render()
        self.assertEqual(len(self.graphics.render_list), 0)
    
    def testRenderNone(self):
        self.assertRaises(TypeError, self.graphics.RenderText, None)
        