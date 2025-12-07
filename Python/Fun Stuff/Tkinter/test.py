equation = "3÷3"

def evaluate(equation):
    """Changes the 'x' to '*' and evaluates the equation."""
    output = ''
    for i in equation:
        if i.lower() == 'x':
            output += '*'
        elif i == '÷':
            output += '/'
        else:
            output += i
            
    return eval(output)
    
answer = evaluate(equation)
print(answer)