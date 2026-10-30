# try:
#     num1 = int(input("Enter first number: "))
#     num2 = int(input("Enter second number: "))

#     print("Answer =", num1 / num2)

# except ZeroDivisionError:
#     print("You cannot divide by zero!")

# print("abc")

# # Multiple Exceptions
# try:
#     num = int(input("Enter a number: "))
#     result = 100/num

# except ValueError:
#     print("Please enter only numbers.")

# except ZeroDivisionError:
#     print("Number cannot be zero.")

# else:
#     print("The result is: {result}")

# finally:
#     print("THIS BLOCK WILL ALWAYS BE EXECUTED")

## File Handling
# try:
#     file = open("students.txt", "r")
#     print(file.read())

# except FileNotFoundError:
#     print("The file does not exist.")

# finally:
#     print("Program Finished")


## else
# try:
#     age = int(input("Enter your age: "))

# except ValueError:
#     print("Age should be a number.")

# else:
#     print("Your age is", age)


# balance = 5000
# try:
#     amount = int(input("Enter withdrawal amount: "))

#     if amount > balance:
#         raise ValueError("Insufficient Balance")

#     balance -= amount
#     print("Transaction Successful")
#     print("Remaining Balance =", balance)

# except ValueError as e:
#     print(e)

# Problem Statement
# Write a Python program to simulate an online shopping checkout system using error handling.
# The program should ask the user to enter the price of a product and the quantity they want to purchase. It should calculate and display the total bill if the inputs are valid.
# Requirements:
# Ask the user to enter the product price and quantity.
# If the user enters text instead of a number, display Invalid input! Please enter numbers only.
# If the product price is zero or negative, display Price must be greater than zero!
# If the quantity is zero or negative, display Quantity must be at least 1!
# If all inputs are valid, calculate the total bill and display Purchase successful!
# Use try, except, else, and finally to handle errors and control the program flow.
# Display Thank you for shopping with us! in every case.



try:
    price = float(input("Enter product price: "))
    quantity = int(input("Enter quantity: "))

    if price <= 0:
        print("Price must be greater than zero!")

    elif quantity <= 0:
        print("Quantity must be at least 1!")

    else:
        total = price * quantity
        print("Total bill: ₹", total)

except ValueError:
    print("Invalid input! Please enter numbers only.")

else:
    if price > 0 and quantity > 0:
        print("Purchase successful!")

finally:
    print("Thank you for shopping with us!")
