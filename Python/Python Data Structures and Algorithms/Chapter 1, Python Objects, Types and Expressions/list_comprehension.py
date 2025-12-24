example = [[1, 2, 3], [4, 5, 6]]

multiples = [x + y for x in example[0] for y in example[1] ]
print(multiples)