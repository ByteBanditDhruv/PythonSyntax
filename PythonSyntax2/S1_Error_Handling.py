try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    print("Answer =", num1 / num2)

except ZeroDivisionError:
    print("You cannot divide by zero!")

print("abc")

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