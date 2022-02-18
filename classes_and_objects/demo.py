#demo on classes and objects
class Dog():
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed
    
    def bark(self):
        return "Woof!"
    
    def __str__(self):
        return f"A {self.age}-year-old {self.breed} called {self.name}"

fido = Dog('Fido', 3, 'Poodle')
print(fido)
print(fido.bark())
#print(getattr(Fido, 'age'))
