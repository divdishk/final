#LCD
"""
function gcd(a, b):
    if b is 0:
        return a
    else:
        return gcd(b, a % b)

function lcm(a, b):
    return (a*b)/gcd(a,b)
function lcd(numerator, denominator):
    return denominator
"""
def gcd(a, b):
    if b == 0:
        return a
    # recursive case: call gcd with b and remainder of a divided by b
    return gcd(b, a % b)

def lcm(a, b):
    return (a * b) // gcd(a, b)

def lcd(numerator, denominator):
    return denominator

numerator = 3
denominator = 6
print("Least common denominator of", numerator, "/", denominator, "is:", lcd(numerator, denominator))
