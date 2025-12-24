lst = [1, 2, 3, 4]
cubes = list(map(lambda x : x**3, lst)) # Maps out the available values to the power of three. (Following the specified condition.)
print(cubes)

filt_list = list(filter(lambda y : y % 2 == 1, lst)) # Filter out the even numbers and return the odd numbers in the list.
print(filt_list)