#LCD(iterations)
def GCD(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def LCM(a, b):
    return (a * b) // GCD(a, b)

def LCD(numerator, denominator):
    return denominator


numerator = 3
denominator = 5
print("Least common denominator of", numerator, "/", denominator, "is:", LCD(numerator, denominator))
