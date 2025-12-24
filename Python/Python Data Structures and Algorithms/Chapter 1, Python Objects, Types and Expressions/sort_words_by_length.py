def process(input, criteria, reverse=False):
    output = sorted(input, key=criteria, reverse=reverse)
    return output

words = 'The quick brown fox jumped over the lazy dogs.'
lst = words.split()

# output = process(lst, len)
    
letters = ['A', 'b', 'g', 'a', 'B', 'Y', 'y', 'W', 'i']
output = process(letters, str.lower)


print(output)