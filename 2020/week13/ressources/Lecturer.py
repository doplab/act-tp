class Lecturer:
    def __init__(self, name, years_experience, full_time):
        ...
        
    def avg_annual_salary(self):
        ...
        
    
class Professor(Lecturer):
    def __init__(self, name, years_experience, monthly_salary, commission, num_committees_served):
        ...
        
    def monthly_payroll(self):
        ...
        
class ParttimeLecturer(Lecturer):
    def __init__(self, name, years_experience, hours_per_month, rate):
        ...
        
    def monthly_payroll(self):
        ...
    
prof1 = Professor("Alexandra", 8, 3000, 200, 4) 
prof2 = ParttimeLecturer("David", 10, 40, 30)

# exemples
print(prof1.avg_annual_salary)
print(prof2.monthly_payroll)