# ## WITHOUT OOPS

# # Student 1
# name1 = "Rahul"
# roll1 = 101
# marks1 = 90

# # # Student 2
# name2 = "Priya"
# roll2 = 102
# marks2 = 95

# print(name1, roll1, marks1)
# print(name2, roll2, marks2)


# class Student:

#     def __init__(self, name, roll, marks):
#         self.name = name
#         self.roll = roll
#         self.marks = marks

# s1 = Student("Rahul", 101, 90)
# s2 = Student("Priya", 102, 95)

# print(s1.name)
# print(s2.name)


# class Student:

#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def display(self):
#         print("Name :", self.name)
#         print("Marks:", self.marks)

# s1 = Student("Rahul", 90)
# s2 = Student("Priya", 95)

# s1.display()
# s2.display()


# class Car:

#     def __init__(self, brand, color):
#         self.brand = brand
#         self.color = color

#     def start(self):
#         print(self.brand, "has started.")

#     def stop(self):
#         print(self.brand, "has stopped.")

# car1 = Car("BMW", "Black")
# car2 = Car("Mercedes", "White")

# car1.start()
# car2.stop()


class Student:
    def __init__(self, name, m1, m2, m3):
        self.name = name
        self.marks = [m1, m2, m3]

    def average(self):
        return sum(self.marks) / 3

    def result(self):
        if self.average() >= 40:
            return "Pass"
        return "Fail"


s1 = Student("Aarav", 98, 100, 90)
s2 = Student("Riya", 30, 40, 35)

print(s1.name, s1.average(), s1.result())
print(s2.name, s2.average(), s2.result())

if s1.average() > s2.average():
    print(s1.name, "has a higher average")
else:
    print(s2.name, "has a higher average")