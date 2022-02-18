'''
Write a program that takes a number and prints the full times table of that number. Do not include 0.
Hint: dont manually set your code to print each number, one by one. Use a loop.
'''

def calc_check_digit(isbn):
    check_dig = 10
    sum = 0
    strng = str(isbn)
    for i in range(0, 12):
        if i % 2 == 0:
            sum += int(strng[i])
        else:
            sum += 3*(int(strng[i]))
    rem = sum % 10
    check_dig -= rem
    return f"ISBN is: {strng[0:3]}-{strng[3]}-{strng[4:7]}-{strng[7:12]}-{check_dig}"

print(calc_check_digit(978030640615))