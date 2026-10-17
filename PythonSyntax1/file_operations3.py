file = open(r"C:\Users\OMOLP028\OneDrive\Desktop\Dhruv\PythonSyntax1\users.csv", "r")

data = file.read()
print(data)

file.close()


file = open(r"C:\Users\OMOLP028\OneDrive\Desktop\Dhruv\PythonSyntax1\users.csv", "r")

header = file.readline()
print(header)

file.close()


file = open(r"C:\Users\OMOLP028\OneDrive\Desktop\Dhruv\PythonSyntax1\users.csv", "r")

for line in file:
    print(line.strip())

file.close()


file = open(r"C:\Users\OMOLP028\OneDrive\Desktop\Dhruv\PythonSyntax1\users.csv", "r")

lines = file.readlines()

print(lines)

file.close()


import csv

with open(r"C:\Users\OMOLP028\OneDrive\Desktop\Dhruv\PythonSyntax1\users.csv", "r") as file:
    reader = csv.reader(file)

    next(reader)  # Skip the header

    for row in reader:
        print(row[0])


import csv

with open(r"C:\Users\OMOLP028\OneDrive\Desktop\Dhruv\PythonSyntax1\users.csv", "r") as file:
    reader = csv.reader(file)

    next(reader)

    for row in reader:
        print(f"{row[0]} {row[1]} earns ₹{row[3]}")