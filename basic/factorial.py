# Factorial of a non-negative integer, is multiplication of all integers smaller than or equal to n in Python.
# we take an example of 5
# so factorial of the 5 = 5 * 4 * 3 * 2 * 1 = 120

num = 5
factorial = 1

for i in range(1, num+1):
    factorial = factorial * i
    
print(f"factorial of {num} is {factorial}.")