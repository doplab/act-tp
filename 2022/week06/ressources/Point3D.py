class Point3D(Point):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.__z = z
        
    def get_z(self):
        ...
    
    def set_z(self, z):
        ...
        
    def vector_representation(self): # représentée sous forme de liste
        ...
        
    def distance_euclidean(self, p2): # i.e norme
        ...
    
    def distance_manhattan(self, p2):
        ...
        
    def distance_minkowski(self, p2, order=3):
        ...
        
    def milieu(self, p2):
        ...