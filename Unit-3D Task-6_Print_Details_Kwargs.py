def print_details(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

print_details(name="Venkatesh", age=19, city="Markapur")