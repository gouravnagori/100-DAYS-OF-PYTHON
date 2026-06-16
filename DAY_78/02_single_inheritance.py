class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def make_sound(self):
        print("Sound made by the animal")

class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="Dog")
        self.breed = breed
        
    def make_sound(self):
        print("Bark!")

d = Dog("Dog", "Doggerman")
d.make_sound()

a = Animal("Dog", "Dog")
a.make_sound()

# Quick Quiz: Implement a Cat class by using the animal class. 
# Add some methods specific to cat


class Animal1:
    def __init__(self,name,species):
        self.name=name
        self.species=species
    def info(self):
       print(f"The Animal of name {self.name} is of species {self.species}.")
        
        
class Cat(Animal1):
    def __init__(self,name,species,breed):
        super().__init__(name,species)
        self.breed=breed
    def info(self):
        print(f"The cat of name {self.name} of species {self.species} if of {self.breed} breed.")
        
a=Animal1("shera","dog")
a.info()
b=Cat("mani","cat","cattie")
b.info()