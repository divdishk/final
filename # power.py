# power
"""
function power(x, e):
    if e == 0:
        return 1
    else if e > 0:
        return x * power(x, e - 1)
    else:  # e < 0
        return 1 / (x * power(x, -e - 1))
"""

def power(x, e):
    if e == 0:
        return 1
    elif e > 0:
        return x * power(x, e - 1)
    else:  # e < 0
        return 1 / (x * power(x, -e - 1))

# Taking user input for base (x) and exponent (e)
x = float(input("Enter the base (x): "))
e = int(input("Enter the exponent (e): "))

# Calculate and print the result
result = power(x, e)
print(f"{x} raised to the power of {e} is: {result}")
