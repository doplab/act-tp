class Point3D(Point):
    def __init__(self, x, y):
        super().__init__(x, y)
        # Rajoutez un nouvel attribut z propre à la classe Point3D
        
    
    # Définir le getter et le setter sur le nouvel attribut z
        
    # Complétez les méthodes suivantes
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