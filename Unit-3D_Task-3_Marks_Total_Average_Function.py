def calculate_marks(m1, m2, m3):
    total = m1 + m2 + m3
    average = total / 3

    return total, average


a = float(input("Enter first subject marks: "))
b = float(input("Enter second subject marks: "))
c = float(input("Enter third subject marks: "))

total, average = calculate_marks(a, b, c)

print("Total Marks:", total)
print("Average Marks:", average)