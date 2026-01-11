class ExampleClass():
    def __init__(self, greet):
        self.greet = greet
        
    def __repr__(self):
        return "A custom object (%r)" % self.greet
    
x = ExampleClass('pizza')
print(x)