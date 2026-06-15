class Employee:
    company = 'Apple'
    def show(self):
        print(f"Employee name is {self.name} and company is {self.company}")
    
    @classmethod
    def changeCompany(cls,newcompany):
        cls.company = newcompany

e1 = Employee()
e1.name = 'rahul'
e1.show()
e1.changeCompany("Nvidia")
e1.show()
print(Employee.company)