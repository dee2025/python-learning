# create a fun for calculate the simple interest
def simple_interest(p, r, t):
    return (p * r * t) / 100

# taking the values from user
principle = int(input("Enter principle amount: "))
rate = int(input("Enter rate: "))
time = int(input("Enter time: "))

# call the function
interest = simple_interest(principle, rate, time)

# print the result
print(f"Simple interest is {interest}.")
