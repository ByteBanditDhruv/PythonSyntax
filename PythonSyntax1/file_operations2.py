import csv

with open(r"C:\Users\OMOLP247\OneDrive\Desktop\dhruv\PythonSyntax1\SUPERHEROES.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)

