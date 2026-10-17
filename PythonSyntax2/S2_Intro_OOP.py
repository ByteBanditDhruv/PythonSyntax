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


class Car:

    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def start(self):
        print(self.brand, "has started.")

    def stop(self):
        print(self.brand, "has stopped.")

car1 = Car("BMW", "Black")
car2 = Car("Mercedes", "White")

car1.start()
car2.stop()