#number of dice sides/rolls
from random import randint as rand

class Rolls():
    def __init__(self, vals):
        self.vals = vals
    
    def __add__(self, dice):
        return Rolls(self.vals + [dice.roll()])

    def __str__(self):
        return str(self.vals)

class Dice():
    def __init__(self, sides):
        self.sides = sides
    
    def roll(self):
        return rand(1, self.sides)
    
    def __add__(self, dice2):
        return Rolls([self.roll(), dice2.roll()])

    def __str__(self):
        return f"A {self.sides} sided die"

d6 = Dice(6)
d20 = Dice(20)
d12 = Dice(12)

print(d6 + d20 + d12)