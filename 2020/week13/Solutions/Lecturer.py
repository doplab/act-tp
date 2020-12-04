class Lecturer:
    def __init__(self, name, years_experience, full_time):
        self.name = name
        self.years_experience = years_experience
        self.full_time = full_time
        
    @property
    def avg_annual_salary(self):
        if self.full_time:
            if self.years_experience < 10:
                return 60000
            
            else:
                return 100000
            
        else:
            return "Salary for part-time lecturers unknown"
        
    
class Professor(Lecturer):
    def __init__(self, name, years_experience, monthly_salary, commission, num_committees_served):
        super().__init__(name, years_experience, True)
        self.monthly_salary = monthly_salary
        self.commission = commission
        self.num_committees_served = num_committees_served
        
    @property
    def monthly_payroll(self):
        return self.monthly_salary + self.commission*self.num_committees_served
        
class ParttimeLecturer(Lecturer):
    def __init__(self, name, years_experience, hours_per_month, rate):
        super().__init__(name, years_experience, False)
        self.hours_per_month = hours_per_month
        self.rate = rate
        
    @property
    def monthly_payroll(self):
        return self.hours_per_month*self.rate 
    
prof1 = Professor("Alexandra", 8, 3000, 200, 4) 
prof2 = ParttimeLecturer("David", 10, 40, 30)

# exemples
print(prof1.avg_annual_salary)
print(prof2.monthly_payroll)