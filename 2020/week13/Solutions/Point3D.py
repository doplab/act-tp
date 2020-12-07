class Point3D(Point):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.__z = z
        
    def get_z(self):
        return self.__z
    
    def set_z(self, z):
        self.__z = z
        
    def vector_representation(self): # represented in the list format
        return [self.__x, self.__y, self.__z]
        
    def distance_euclidean(self, p2): # i.e norme
        other_x = p2.get_x()
        other_y = p2.get_y()
        other_z = p2.get_z()
        return math.sqrt((self.__x - other_x)**2 + (self.__y - other_y)**2 + (self.__z - other_z)**2)
    
    def distance_manhattan(self, p2):
        other_x = p2.get_x()
        other_y = p2.get_y()
        other_z = p2.get_z()
        return sum((abs(self.__x - other_x), abs()), abs(self.__y - other_y), abs(self.__z - other_z))
        
    def distance_minkowski(self, p2, order=3):
        other_x = p2.get_x()
        other_y = p2.get_y()
        other_z = p2.get_z()
        return sum((abs(self.__x - other_x)**order), abs(self.__y - other_y)**order,\
                   abs(self.__z - other_z)**order)**(1/order)
        
    def milieu(self, p2):
        other_x = p2.get_x()
        other_y = p2.get_y()
        other_z = p2.get_z()
        
        x_M = (self.__x + other_x)/2
        y_M = (self.__y + other_y)/2
        z_M = (self.__z + other_z)/2
        return Point3D(x_M, y_M, z_M) # renvoie un point!
        
        
point1 = Point3D(1, 2, 3)
point2 = Point3D(3, 4, 5)

# exemple
point1.vector_representation()  