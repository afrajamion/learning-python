'''
Create a new Python file and write a program that does the following:
- Asks for an input from the user as a mark.
- If the mark is greater that 85 print "Distinction"
- If the mark is between 65 and 85 print "Pass"
- Anything else print "Fail"
Try to do this both with and without elif statements.
'''

valid = False
while not valid:
    mark = int(input("Enter a mark: "))
    valid = mark <= 100

# With elif
# if mark > 85:
#     print("Distinction")
# elif mark >= 65:
#     print("Pass")
# else:
#     print("Fail")

# Without elif
if mark > 85:
    print("Distinction")
else:
    if mark >= 65:
        print("Pass")
    else:
        print("Fail")