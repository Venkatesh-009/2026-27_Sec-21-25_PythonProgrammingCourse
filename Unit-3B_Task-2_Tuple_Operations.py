
# Program to demonstrate tuple operations

# Creating two tuples
t1 = (10, 20, 30)
t2 = (40, 50, 60)

# 1. Concatenation
t3 = t1 + t2
print("Concatenation:", t3)

# 2. Slicing
print("Slicing:", t3[1:4])

# 3. Unpacking
a, b, c = t1
print("Unpacking:")
print("a =", a)
print("b =", b)
print("c =", c)
