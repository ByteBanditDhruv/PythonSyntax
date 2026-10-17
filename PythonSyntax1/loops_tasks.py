# # Multiplication Tables
# num = int(input("Enter a number: "))

# for i in range(1, 11):
#     print(num, "x", i, "=", num * i)

# # Guess the Number
# secret = 7
# guess = 0

# while guess != secret:
#     guess = int(input("Guess the number: "))

#     if guess < secret:
#         print("Too low!")
#     elif guess > secret:
#         print("Too high!")
#     else:
#         print("Correct!")

# print("Game Over!")

# # PATTERN 1
# for i in range(1,6):
#     print("*\t" * i)

# # PATTERN 2
# n = int(input("Enter Number of Iterations: "))

# for i in range(1, n):
#     print("__" * ((n-1) - i) + "* " * i)

# # PATTERN 3
n = int(input("Enter Number of Iterations: "))

for i in range(1, n + 1):
    print("  " * (n - i) + "* " * (2 * i - 1))