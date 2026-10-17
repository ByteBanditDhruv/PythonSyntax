num1 = int(input("Enter Number 1"))
num2 = int(input("Enter Second Number"))

operator = input("Enter the Operator: ")

if operator == '+':
    print(num1 + num2)

elif operator == '-':
    print(num1 - num2)

elif operator == '*':
    print(num1*num2)

elif operator == '/':
    print(num1/num2)

else:
    print("The Input is not valid")