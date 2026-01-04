class Employee(object):
    numEmployee = 0
    def __init__(self, name, rate):
        self.owed = 0
        self.name = name
        self.rate=rate
        self.numEmployee += 1

    def __del__(self):
        Employee.numEmployee -= 1

    def hours(self, numHours):
        self.numHours = numHours
        self.owed = self.numHours * self.rate
        return(f"%s hours worked ({self.name})." % numHours)

    def pay(self):
        self.owed = self.numHours * self.rate
        return(f"Payed {self.name} {self.owed} at a rate of {self.rate} per hour for {self.numHours} hours.")
    
michelle = Employee('michelle', 100)
hours_worked = michelle.hours(10)
payment = michelle.pay()

print(hours_worked)
print(payment)