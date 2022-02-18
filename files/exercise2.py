'''
Create a new Python file which does the following:

Edits your "teams.txt" file so that the top line is replaced with "This is a new line".
Print out the edited file line by line.
'''

with open('teams.txt', 'r') as teams:
    lines = teams.readlines()
    lines[0] = "This is a new line\n"

with open('teams.txt', 'w') as teams:
    teams.writelines(lines)

with open('teams.txt', 'r') as teams:
    for line in teams.readlines():
        print(line.strip())