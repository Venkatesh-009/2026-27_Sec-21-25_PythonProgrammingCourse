def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


num1 = 24
num2 = 36

result = gcd(num1, num2)

print("GCD of", num1, "and", num2, "is:", result)