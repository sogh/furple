"""
The simulation class encapsulates all the things in our virtual world that change over time.
A tick is one step in time in the simulation.
"""
class Simulation:
    def __init__(self):
        self.ticks = 0
        self.updateables = []

    def Update(self):
        self.ticks = self.ticks + 1
        for i in self.updateables:
            i.Update(self.ticks)

    def AddUpdateable(self, updateable):
        self.updateables.append(updateable)        


    