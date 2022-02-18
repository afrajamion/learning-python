'''
Create 2 new Python files. In one file, 
write a function that will generate a 
number between 1 and 6. Make this a module 
called dice. In the second file, use the 
dice module to simulate throwing 2 dice and 
print the values you get from the dice.
'''

from random import randint as rand

def roll():
    return rand(1, 6)

def main():
    input("Press ENTER to roll: ")
    print(roll())

if __name__ == '__main__':
    main()