# Import time to track how long the.
import time

# The following functions do the same thing. One uses iteration, one uses recursion.
#Iteration
def iterTest(low, high):
    while low <= high:
        # print(low, end=' ')
        low += 1

# Recursion
def recurTest(low, high):
    if low <= high:
        # print(low, end=' ')
        recurTest(low+1, high)

low, high = 1, 996

time1 = time.time()
iterTest(low, high)
print('\nTime taken for iterative function: %f' % (time.time() - time1))

time1 = time.time()
recurTest(low, high)
print('\nTime taken for recursive function: %f' % (time.time() - time1))