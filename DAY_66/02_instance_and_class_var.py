class Employee:
    company_name = 'OptiMeal'
    noofemp = 0
    def __init__(self,name):
        self.name = name
        self.raise_amount = 0.3
        Employee.noofemp += 1

    def show(self):
        print(f"The name of the employee is {self.name} and working in {self.noofemp} sized company {self.company_name} and their raise amount is {self.raise_amount}")

emp1 = Employee("Ragu")
emp1.raise_amount = 0.54
emp1.company_name = 'Google'
emp1.show()
# Employee.show(emp1)
# Employee.company_name = 'Microsoft'
emp2 = Employee("Neha")
emp2.show()
        


