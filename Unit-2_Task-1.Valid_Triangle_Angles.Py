a=int(input("Enter the first side of triangle: "))
b=int(input("Enter the second side of triangle: "))
c=int(input("Enter the third side of triangle: "))
if a>0 and b>0 and c>0 and a+b+c==180:
    print("The triangle is valid.")
else:
    print("The triangle is not valid.")