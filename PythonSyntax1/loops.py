# Loops are used to execute a block of code repeatedly until a specified condition is met. Instead of writing the same code multiple times, loops automate repetitive tasks, making programs shorter and more efficient.

# FOR LOOP
# A for loop is used to iterate over a sequence such as a list, tuple, string, dictionary, or range.
# for variable in sequence:
#     statements

# for i in range(1, 6):
#     print(i)


# name = "Python"

# for letter in name:
#     print(letter)

# fruits = ["Apple", "Banana", "Mango"]

# for fruit in fruits:
#     print(fruit)

# The range() Function
# The range() function generates a sequence of numbers. range(start, stop, step)

# for i in range(5):
#     print(i)

for i in range(2, 8):
    print(i)

# for i in range(2, 11, 2):
#     print(i)


# WHILE LOOP
# A while loop executes as long as the given condition is True.
    # while condition:
    # statements

# count = 1

# while count <= 5:
#     print(count)
#     count += 1
import time
for i in range(10, 0, -1):
    print(i)
    time.sleep(1)

print("Liftoff!")
print("🚀 Rocket Launched!")

# count = 10

# while count > 0:
#     print(count)
#     count -= 1

# print("🚀 Rocket Launched!")