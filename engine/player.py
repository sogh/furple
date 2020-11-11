from engine.point import Point

class Player:
    def __init__(self):
        self.__position = Point(0,0)

    @property
    def position(self):
        return self.__position

    def wacky_move(self):
        self.__position.x = self.__position.x + 1

    def move(self,direction):
        if direction.lower() == 'north' or direction.lower() == 'n':
            self.__position.y = self.__position.y + 1
        elif direction.lower() == 'south' or direction.lower() == 's':
            self.__position.y = self.__position.y - 1
        elif direction.lower() == 'east' or direction.lower() == 'e':
            self.__position.x = self.__position.x + 1
        elif direction.lower() == 'west' or direction.lower() == 'w':
            self.__position.x = self.__position.x - 1
        else:
            print('SPEAK ENGLISH')