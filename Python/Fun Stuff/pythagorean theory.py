from math import sqrt

def confirm_integer(user_input):
    ''' A while loop to make sure the input is an integer.'''
    while True:
        # if user_input:
        #     try:
        #         user_input = int(user_input)
        #         break
        #     except ValueError:
        #         user_input = input('\nPlease enter a number.\n')

        # else:
        #         user_input = input('\nPlease enter a number.\n')
                

            
a  = input('\nEnter a number: \n')
confirm_integer(a)

b  = input('\nEnter another number: \n')
confirm_integer(b)

# Implement Pythagora's theory of right angles (a**2 + b**2 = c**2).
c = sqrt(int(a)**2 + int(b)**2)

print('C is', + c)