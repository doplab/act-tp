class Enseignant:
    def __init__(self, name, years_experience, full_time):
        self.name = name
        self.years_experience = years_experience
        self.full_time = full_time
        
    def salaire_annuel_moyen(self):
        if self.full_time:
            if self.years_experience < 10:
                return 60000
            
            else:
                return 100000
            
        else:
            return "Le salaire annuel ne s'applique pas aux collaborateurs"
        
    
class Professeur(Enseignant):
    def __init__(self, name, years_experience, monthly_salary, commission, num_committees):
        super().__init__(name, years_experience, True)
        self.monthly_salary = monthly_salary
        self.commission = commission
        self.num_committees = num_committees
        
    def paye_mensuelle(self):
        return self.monthly_salary + self.commission*self.num_committees
        
class Collaborateur(Enseignant):
    def __init__(self, name, years_experience, hours_per_month, rate):
        super().__init__(name, years_experience, False)
        self.hours_per_month = hours_per_month
        self.rate = rate
        
    def paye_mensuelle(self):
        return self.hours_per_month*self.rate 
    
prof1 = Professeur("Alexandra", 8, 3000, 200, 4) 
prof2 = Collaborateur("David", 10, 40, 30)

# exemples
print(prof1.salaire_annuel_moyen())
print(prof2.paye_mensuelle())