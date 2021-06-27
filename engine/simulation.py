"""
The simulation class encapsulates all the things in our virtual world that change over time.
A tick is one step in time in the simulation.
"""
import pygame.time

class Simulation:
    def __init__(self):
        self.updateables = []

    def Update(self):
        for i in self.updateables:
            i.Update(pygame.time.get_ticks())

    def AddUpdateable(self, updateable):
        self.updateables.append(updateable)


    