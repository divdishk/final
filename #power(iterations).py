#power(iterations)
def power(x, e):
    result = 1
    if e < 0:
        x = 1 / x
        e = -e
    for _ in range(e):
        result *= x
    return result

# Taking user input for base (x) and exponent (e)
x = float(input("Enter the base (x): "))
e = int(input("Enter the exponent (e): "))

# Calculate and print the result
result = power(x, e)
print(f"{x} raised to the power of {e} is: {result}")
