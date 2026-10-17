import bank_module as bank

while True:
    print("-----BANK MENU-----")
    print("1. CREATE ACCOUNT")
    print("2. LOGIN")
    print("3. EXIT")

    choice = int(input("Enter your Choice: "))

    if choice == 1:
        bank.create_account()

    elif choice == 2:
        user = bank.login()
        if user:
            while True:
                print("----- USER MENU -----")
                print("1. Deposit")
                print("2. Withdraw")
                print("3. Check Balance")
                print("4. Logout")

                option = int(input("Enter your Choice: "))

                if option == 1:
                    bank.deposit(user)
                    
                elif option == 2:
                    bank.withdrawal(user)

                elif option == 3:
                    print("Balance:", bank.accounts[user]["balance"])

                elif option == 4:
                    print("Logged Out Successfully!")
                    break

                else:
                    print("Invalid Choice!")

    elif choice == 3:
        print("Thank You!!")
        break



# Create a Python module named math_tools.py that contains two functions:
# add(a, b) — returns the sum of two numbers.
# multiply(a, b) — returns the product of two numbers.
# Then create another Python file named main.py that imports the math_tools module and uses these functions to calculate and
# display the results.


# Example Input:
# 5
# 3
# Expected Output:
# Sum: 8
# Product: 15


# # math_tools.py

# def add(a, b):
#     return a + b

# def multiply(a, b):
#     return a * b


# # main.py

# import math_tools
# print(math_tools.add(10,8))
# print(math_tools.multiply(7,3))