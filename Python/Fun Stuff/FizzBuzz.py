def fizzbuzz():
    for number in range(1, 201):
        # number is divisible by 3 and 5.
        if number % 3 == 0 and number % 5 == 0:
            output = 'FizzBuzz'
        
        # if the number is divisible by 3.
        elif number % 3 == 0:
            output = 'Fizz'
            
        # if the number is divisible by 5
        elif number % 5 == 0:
            output = 'Buzz'
            
        else:
             output = number
             
        print(output)
    
fizzbuzz()