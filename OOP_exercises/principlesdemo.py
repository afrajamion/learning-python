#demo
from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @abstractmethod
    def make_noise(self):
        pass

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def make_noise(self):
        return "Woof!"

    def __str__(self):
        return f"A {self.age}-year-old {self.breed} called {self.name}"

class Cat(Animal):
    def make_noise(self):
        return "Meow!"

    def __str__(self):
        return f"A {self.age}-year-old cat called {self.name}"

fido = Dog('Fido', 3, 'Poodle')
print(fido)
print(fido.make_noise())
felix = Cat('Felix', 5)
print(felix)
print(felix.make_noise())