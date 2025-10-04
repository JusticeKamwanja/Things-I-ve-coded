'''
ASK THE USER FOR A NUMBER
CHECK THAT NUMBER
GIVE AN OUTPUT
'''

from math import sqrt
from math import ceil

# A prime number is divisible by 1 and itself.

def check_prime(number):
    number = int(number)
    if number <= 1:
        output = 'NOT PRIME'
        
    else:
        numbers = list(range(2, ceil(sqrt(number))))
        for i in numbers:
            if number % i == 0:
                output = 'NOT PRIME'
            elif number % i != 0:
                output = 'PRIME'
        
        print('\n')
        print(str(number) + ' is ' + output)
        print('\n')
    
check_prime(39)