from engine.point import Point

class Player:
    def __init__(self):
        self.__position = Point(0,0)

    @property
    def position(self):
        return self.__position

    def wacky_move(self):
        self.__position.x = self.__position.x + 1