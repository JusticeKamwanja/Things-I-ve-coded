a = 10
b = 20

def my_func():
    global a
    
    a = 11
    
    b = 21
    
my_func()

print(a)
print(b)