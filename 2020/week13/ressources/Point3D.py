class Point3D(Point):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.__z = z
        
    @property # decorator, nouvelle dimension
    def ...:
        ...
    
    @z.setter 
    def ...:
        ...
        
    @property
    def vector_representation(self): # represented in the list format
        ...
        
    def euclidean_distance(self, p2): # i.e norme
        ...
    
    def manhattan_distance(self, p2):
        ...
        
    def minkowski_distance(self, p2, order=3):
        ...
        
    def milieu(self, p2):
        ...