'''
def is_prime(x):
    if x < 2:
        return False
    else:
        for n in range(2, x-1):
            if x % n = 0:
                return False
            return True
Test the is_prime function with 2, 3, 4, 5, 6, 7, 15, 20 & 25
'''

import pdb
def is_prime(x):
    if x < 2:
        return False
    else:
        for n in range(2, x-1):
            if x % n == 0:
                return False
        return True

pdb.set_trace()
# Test the is_prime function with 2, 3, 4, 5, 6, 7, 15, 20 & 25
for i in (2, 3, 4, 5, 6, 7, 15, 20, 25):
    print(is_prime(i))