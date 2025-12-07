nest = [
    ['apples', 45, 10],
    ['oranges', 15, 6],
    ['mangoes', 20, 11]
]
for item in nest:
    fruit = item[0]
    price = item[1]
    quantity = item[2]
    
    output = 'I want ' + str(quantity) + ' ' + fruit + ', and they go for ' + str(price) + ' shillings each.'
    
    print(output)