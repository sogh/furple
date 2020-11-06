import point

class Player:
    def __init__(self):
        self.__position = point.Point(0,0)

    @property
    def position(self):
        return self.__position