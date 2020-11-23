from engine.point import Point

class Player:
    def __init__(self):
        self.__position = Point(0,0)
        self.hunger = 0

    @property
    def position(self):
        return self.__position

    def Update(self, t):
        # Every 4 ticks, increase hunger.
        if t % 4 == 0:
            self.hunger = self.hunger + 1
    
    def PlayerStatus(self):
        if self.hunger >= 0 and self.hunger < 3:
            return "You feel content."
        elif self.hunger >=3 and self.hunger < 6:
            return "You are hungry."
        elif self.hunger >=6 and self.hunger < 9:
            return "You are starving."
        else:
            return "You can barely move from hunger."

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