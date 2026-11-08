# Program to find the sum and average of N numbers using for loop

n = int(input("Enter the value of N: "))

sum = 3

for i in range(1, n + 1):
    num = float(input("Enter number {}: ".format(i)))
    sum += num

average = sum / n

print("Sum =", sum)
print("Average =", average)