'''
ISBN's (International Standard Book Numbers) are identifiers for books.

The ISBN is a thirteen-digit code.

The last digit is a check number calculated as follows:

The first 12 digits are taken Starting at index 0, if the index is even - add it, and if the index is odd – multiply the digit by three then add it.

From the sum find the remainder after dividing by 10. 10 minus the remainder give us the check digit

In other words the following algebra would give us the check digit:

digit_12 = 10 - (( digit_0 + (3 x digit_1) + digit_2 + (3 x digit_3) + digit_4 + (3 x digit_5) + digit_6 + (3 x digit_7) + digit_8 + (3 x digit_9) + digit_10 + (3 x digit_11) ) % 10)
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