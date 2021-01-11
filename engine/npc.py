from engine.point import Point
from random import choice

possible_names = ['steve', 'mark', 'jill', 'edna']
class NPC:
    """Representation of a basic NPC."""
    def __init__(self, x_loc = 0, y_loc = 0):
        #self.possible_names = ['steve', 'mark', 'jill', 'edna']
        self.__position = Point(x_loc, y_loc)
        self.name = choice(possible_names)
        possible_names.remove(self.name)

    def recall_name(self):
        return self.name

    def greet(self):
        return f"{self.name.title()}:  Hi!, my name is {self.name.title()}!"