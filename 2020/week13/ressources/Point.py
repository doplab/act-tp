import math

class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y
    
    @x.setter
    def x(self, x):
        self.__x = x

    @y.setter
    def y(self, y):
        self.__y = y

    def euclidean_distance(self, p2):
        return math.sqrt((self.__x - p2.get_x())**2 + (self.__y - p2.get_y())**2)

    def milieu(self, p2):
        x_M = (self.__x + p2.get_x()) /2
        y_M = (self.__y + p2.get_y()) / 2
        M = Point(x_M, y_M)
        return M

    def __str__(self):
        return "Les coordonnées du point sont: x="+str(self.get_x())+", y="+str(self.get_y())