# Binary(iteration)
def toBinary(n):
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n //= 2
    return binary if binary else "0"


number =57
print("Binary representation of", number, "is:", toBinary(number))
