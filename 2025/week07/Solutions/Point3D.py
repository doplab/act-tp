import math
import Point

class Point3D(Point):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self._z = z
        
    def get_z(self):
        return self._z
    
    def set_z(self, z):
        self._z = z
        
    def vector_representation(self): # représentée sous forme de liste
        return [self._x, self._y, self._z]
        
    def distance_euclidean(self, p2): # i.e norme
        other_x = p2.get_x()
        other_y = p2.get_y()
        other_z = p2.get_z()
        return math.sqrt((self._x - other_x)**2 + (self._y - other_y)**2 + (self._z - other_z)**2)
    
    def distance_manhattan(self, p2):
        other_x = p2.get_x()
        other_y = p2.get_y()
        other_z = p2.get_z()
        return sum([abs(self._x - other_x), abs(self._y - other_y), abs(self._z - other_z)])
        
    def distance_minkowski(self, p2, order=3):
        other_x = p2.get_x()
        other_y = p2.get_y()
        other_z = p2.get_z()
        return sum([abs(self._x - other_x)**order, abs(self._y - other_y)**order, abs(self._z - other_z)**order])**(1/order)
        
    def milieu(self, p2):
        other_x = p2.get_x()
        other_y = p2.get_y()
        other_z = p2.get_z()
        
        x_M = (self._x + other_x)/2
        y_M = (self._y + other_y)/2
        z_M = (self._z + other_z)/2
        return Point3D(x_M, y_M, z_M) # renvoie un point!
        
        
point1 = Point3D(1, 2, 3)
point2 = Point3D(3, 4, 5)

# exemple
point1.vector_representation()  