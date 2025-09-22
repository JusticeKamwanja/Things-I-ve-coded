name = input('What is your name?').title()
message = f'Hello there, {name}?'

while True:
  var = input('Print name? (y/n) : /n')
  if var.lower() == 'y':
    print(message)
  elif var.lower() == 'n':
    return None
  else:
    print("Respond with, 'y' or 'n'.")