'''
Create a Python file which does the following:

Opens a new text file called "teams.txt" and adds the names of 5 sports teams.
Reads and displays the names of the 1st and 4th team in the file.
'''

with open('teams.txt', 'w') as teams:
    teams.writelines(['Manchester City\n', 'Chelsea\n', 'Liverpool\n', 'Sale Sharks\n', 'Wigan Warriors'])

with open('teams.txt', 'r') as teams:
    lines = [line.strip() for line in teams.readlines()]
    print(lines[0], lines[3], sep='\n')
