class Enseignant:
    def __init__(self, name, years_experience, full_time):
        ...   
    def salaire_annuel_moyen(self):
        ...
        
class Professeur(Enseignant):
    def __init__(self, name, years_experience, monthly_salary, commission, num_committees):
        ...
    def paye_mensuelle(self):
        ...
        
class Collaborateur(Lecturer):
    def __init__(self, name, years_experience, hours_per_month, rate):
        ...
    def paye_mensuelle(self):
        ...
    
prof1 = Professeur("Alexandra", 8, 3000, 200, 4) 
prof2 = Collaborateur("David", 10, 40, 30)
# exemples
print(prof1.salaire_annuel_moyen())
print(prof2.paye_mensuelle())