def add_numbers(*args):
    total = 0

    for num in args:
        total = total + num

    return total

result = add_numbers(10, 20, 30, 40, 50)

print("Sum of numbers:", result)