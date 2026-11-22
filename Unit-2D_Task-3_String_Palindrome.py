str1 = input("Enter a string: ")

rev = str1[::-1]

if str1 == rev:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")