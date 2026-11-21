balance = 1000

def deposit(amount):
    global balance
    balance = balance + amount
    print("Deposited Amount:", amount)
    print("Updated Balance:", balance)

def local_balance():
    balance = 500
    print("Local Balance:", balance)

deposit(500)
local_balance()

print("Final Bank Balance:", balance)