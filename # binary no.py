# binary no.
"""p-code: 
function toBinary(n):
    if n == 0:
        return ""
    else:
        return toBinary(n//2) + str(n%2)
"""

def toBinary(n):
    if n ==0:
        return ""
    else:
        return toBinary(n//2)+ str(n%2)

number = 10
print("Binary representation of", number, "is:", toBinary(number))