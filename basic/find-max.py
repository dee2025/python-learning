# we will explore various methods to find maximum of two numbers in Python.

num1 = 10
num2 = 20

maxValue = 0

# FIRST METHOD (IF... ELSE)
if num1 > num2:
    maxValue = num1
else:
    maxValue = num2
print(f"FIRST MEHOD: {maxValue}")


# SECOND METHOD (TERNARY OPERATOR)
maxValue = num1 if num1 > num2 else num2
print(f"SECOND METHOD: {maxValue}")


# IN-BUILT FUNCTION
maxValue = max(num1, num2)
print(f"THIRD METHOD: {maxValue}")
