class Point3D(Point):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.__z = z
        
    @property # decorator 
    def z(self):
        return self.__z
    
    @z.setter 
    def z(self, z):
        self.__z = z
        
    @property
    def vector_representation(self): # represented in the list format
        return [self.x, self.y, self.z]
        
    def euclidean_distance(self, p2): # i.e norme
        other_x = p2.x
        other_y = p2.y
        other_z = p2.z
        return math.sqrt((self.x - other_x)**2 + (self.y - other_y)**2 + (self.z - other_z)**2)
    
    def manhattan_distance(self, p2):
        other_x = p2.x
        other_y = p2.y
        other_z = p2.z
        return sum((abs(self.x - other_x), abs()), abs(self.y - other_y), abs(self.z - other_z))
        
    def minkowski_distance(self, p2, order=3):
        other_x = p2.x
        other_y = p2.y
        other_z = p2.z
        return sum((abs(self.x - other_x)**order), abs(self.y - other_y)**order,\
                   abs(self.z - other_z)**order)**(1/order)
        
    def milieu(self, p2):
        other_x = p2.x
        other_y = p2.y
        other_z = p2.z
        
        x_M = (self.x + other_x)/2
        y_M = (self.y + other_y)/2
        z_M = (self.z + other_z)/2
        return Point3D(x_M, y_M, z_M) # renvoie un point!
        
        
point1 = Point3D(1, 2, 3)
point2 = Point3D(3, 4, 5)

# exemple
point1.vector_representation  