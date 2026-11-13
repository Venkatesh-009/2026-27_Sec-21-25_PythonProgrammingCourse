
# Program to demonstrate set membership and methods

# Creating a set
s = {10, 20, 30, 40}

print("Original Set:", s)

# Membership testing
print("Is 20 present?", 20 in s)
print("Is 50 present?", 50 not in s)

# Add method
s.add(50)
print("After adding 50:", s)

# Remove method
s.remove(30)
print("After removing 30:", s)

# Discard method
s.discard(100)
print("After discarding 100:", s)
