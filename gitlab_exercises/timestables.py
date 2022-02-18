'''
Write a program that takes a number and prints the full times table of that number. Do not include 0.
Hint: dont manually set your code to print each number, one by one. Use a loop.
'''

def timestable(num):
    i = 1
    while i <= num:
        output = ""
        for x in range(1, num+1):
            ix = i*x
            output += f"{ix}        "
        print(output)
        i += 1 

u_num = int(input("Please enter an integer: "))
timestable(u_num)