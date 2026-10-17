accounts = {}

def create_account():
    username = input("Enter your name: ")
    password = input("Enter your password: ")
    balance = 500
    
    accounts[username] = {
        "password": password,
        "balance": balance
    }
    
    print("Account is Created")
    
    
def login():
    username = input("USERNAME: ")
    password = input("PASSWORD: ")
    
    if username in accounts and accounts[username] ["password"] == password:
        print("LOGIN SUCCESSFUL!!")
        return username
    else:
        print("!!INVALID USERNAME OR PASSWORD!!")
        return None
    
def deposit(username):
    amount = int(input("Enter the Amount to be Deposited: "))
    accounts[username] ["balance"] += amount
    print("Amount Deposited Successfully")
    
def withdrawal(username):
    amount = int(input("Enter the Amount to be Withdrawn: "))
    accounts[username] ["balance"] -= amount
    print("Amount Withdrawn Successfully")