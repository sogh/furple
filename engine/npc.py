from engine.point import Point

class NPC:
    """Representation of a basic NPC."""
    def __init__(self, x_loc = 0, y_loc = 0, name='default'):
        self.__position = Point(x_loc, y_loc)
        self.name = name

    @property
    def position(self):
        return self.__position


    def recall_name(self):
        return self.name

    def greet(self):
        return f"{self.name.title()}:  Hi!, my name is {self.name.title()}!"