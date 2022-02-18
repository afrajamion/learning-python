'''
Exercise- Write a program which:
- Asks the user to input a space-separated list of names
- Ensures each name is correctly cased and splits the string 
into a list of names
- Joins the names back together with a separator of your
choosing, and prints the result
'''

# making it comma-separated allows for firstname + surname
names = input("Enter comma-separated list of names: ") 
# splitting on commas
namelist = names.title().split(',') 
print(' \U0001F642 '.join(namelist))