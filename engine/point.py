class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, value):
        self.__x=value

    @property
    def y(self):
        return self.__x
    @y.setter
    def y(self, value):
        self.__y=value

    def toString(self):
        return f"({self.__x},{self.__y})"