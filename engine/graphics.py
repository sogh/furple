import pygame.display
import pygame.font
from pygame.color import Color
from engine.point import Point

BLACK = Color(0,0,0)
WHITE = Color(255,255,255)

class Graphics:
    def __init__(self, screen_width=800, screen_height=600):
        pygame.display.init()
        self.screen = pygame.display.set_mode([screen_width, screen_height])

        pygame.font.init()
        self.font = pygame.font.SysFont('Arial', 16)
        self.font_color = WHITE
        self.player_font_color = Color(200,200,255)

        self.render_list = []        
        self.prompt = ""
        self.player_input = ""

    def RenderText(self, s):
        if s is None:
            raise TypeError('RenderText only takes String-like arguments.')
        self.render_list.append(self.font.render(s, True, self.font_color))
    
    def RenderPrompt(self, prompt, current_input):
        self.prompt = prompt
        self.player_input = current_input

    def Render(self):
        self.screen.fill(BLACK)
        y = 0
        for r in self.render_list:
            # Fancy renderer, ray tracing coming soon.
            # print(r)
            self.screen.blit(r, dest=(0, y))
            y += self.font.get_linesize()
        self.render_list = []      
        self.screen.blit(self.font.render(self.prompt + self.player_input, True, self.player_font_color), dest=(0, self.screen.get_height() - self.font.get_linesize()))
        pygame.display.flip()
