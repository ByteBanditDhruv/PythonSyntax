# # IF STATEMENT
# # if condition:
# #     statements

# age = 20

# if age >= 18:
#     print("You are eligible to vote.")


# # if...else Statement -> The else block executes when the condition is False.
# # if condition:
# #     statements
# # else:
# #     statements

# num = int(input("Enter a number: "))

# if num % 2 == 0:
#     print("Even Number")
# else:
#     print("Odd Number")


# if...elif...else Statement
# if condition1:
#     statements
# elif condition2:
#     statements
# elif condition3:
#     statements
# else:
#     statements

# marks = int(input("Enter your Marks: "))

# if marks >= 90 and marks <= 100:
#     print("Grade A")
# elif marks >= 75 and marks <= 89:
#     print("Grade B")
# elif marks >= 50 and marks <= 74:
#     print("Grade C")
# else:
#     print("Fail")


# # Simple Calculator
# num1 = float(input("Enter First Number: "))
# num2 = float(input("Enter Second Number: "))

# operator = input("Enter Operator (+, -, *, /): ")

# if operator == "+":
#     print("Result =", num1 + num2)

# elif operator == "-":
#     print("Result =", num1 - num2)

# elif operator == "*":
#     print("Result =", num1 * num2)

# elif operator == "/":
#     if num2 != 0:
#         print("Result =", num1 / num2)
#     else:
#         print("Cannot divide by zero.")

# else:
#     print("Invalid Operator")


# # ATM Withdrawal System1
correct_pin = 1234
balance = 10000

pin = int(input("Enter your ATM PIN: "))

if pin == correct_pin:
    amount = float(input("Enter withdrawal amount: ₹"))

    if amount <= balance:
        balance = balance - amount
        print("\nTransaction Successful")
        print("Please Collect Your Cash")
        print("Remaining Balance: ₹", balance)
        print("Thank You! Please Collect Your Card.")
    else:
        print("\nInsufficient Balance")
else:
    print("\nInvalid PIN")