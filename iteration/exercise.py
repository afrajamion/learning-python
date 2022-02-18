'''
Write a while loop which asks for the names of 5 
people, and for each person prints their name 
followed by the text "is awesome!"
'''

# While-loop
i = 0
while i < 5:
    name = input("Enter a name: ")
    print(name, "is awesome!")
    i += 1

# for-loop
for i in range(5):
    name = input("Enter a name: ")
    print(name, "is awesome!")

# Bit o' both
names = []
while len(names) < 5:
    name = input("Enter a name: ")
    names.append(name)

for name in names:
    print(name, "is awesome!")

# or, in one line:
print('\n'.join([name + ' is awesome!' for name in names]))