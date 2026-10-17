# A function is a reusable block of code that performs a specific task.
#
# Instead of writing the same code multiple times, we create the ability once and use it whenever needed.
#
# Python provides:
#
# 1. Built-in Functions
#    Examples: print(), len(), input()
#
# 2. User-defined Functions
#    Functions that WE create using the def keyword.


# 1. CREATING A FUNCTION
# Syntax:
# def function_name():
#     statements

# def iron_man():
#     print("I am Iron Man!")

# # # Calling the function
# iron_man()

# # We can call the same function multiple times
# iron_man()
# print("Hello World")
# iron_man()


# 2. FUNCTION WITH PARAMETERS

# Parameters allow us to pass information into a function.
# Syntax:
# def function_name(parameter):
#     statements

# def greet(name):
#     print("Hello,", name)

# greet("Iron Man")
# greet("Thor")
# greet("Hulk")


# 3. FUNCTION WITH MULTIPLE PARAMETERS

# Example:
# Iron Man calculates the combined power of two Avengers.

# def calculate_power(hero1, hero2):
#     print("Combined Power =", hero1 + hero2)

# calculate_power(90, 80)


# 4. FUNCTION WITH RETURN

# Some functions don't just print something.
# They can CALCULATE something and RETURN the answer.
#
# Syntax:
# def function_name():
#     return value

# def hulk_power(strength):
#     return strength * 2

# result = hulk_power(6)

# print("Hulk Power =", result)


# 5. ANOTHER RETURN EXAMPLE

# Iron Man wants to calculate his total suit power.

# def suit_power(arc_reactor, armor):
#     return arc_reactor + armor

# power = suit_power(100, 50)

# print("Iron Man's Suit Power =", power)


# 6. VARIABLE SCOPE

# Variables created INSIDE a function are called LOCAL VARIABLES.
# They can normally be used only inside that function.


# def thor():
#     hammer_power = 100
#     print("Thor's Hammer Power =", hammer_power)

# thor()

# We cannot normally access hammer_power here
# because it belongs to the thor() function.


# 7. GLOBAL VARIABLE

# A variable created OUTSIDE a function is a GLOBAL VARIABLE.
# It can be accessed throughout the program.

# avengers_power = 1000

# def avengers():
#     print("Total Avengers Power =", avengers_power)

# avengers()