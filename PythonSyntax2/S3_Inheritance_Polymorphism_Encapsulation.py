# # INHERITANCE
# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

#     def show_details(self):
#         print("Employee:", self.name)
#         print("Salary:", self.salary)


# class Developer(Employee):
#     def __init__(self, name, salary, language):
#         super().__init__(name, salary)
#         self.language = language

#     def show_language(self):
#         print("Programming Language:", self.language)


# dev = Developer("Dhruv", 60000, "Python")

# dev.show_details()
# dev.show_language()

# # POLYMORPHISM
# class Employee:
#     def work(self):
#         print("Employee is working.")


# class Developer(Employee):
#     def work(self):
#         print("Developer is writing code.")


# class Manager(Employee):
#     def work(self):
#         print("Manager is managing the team.")


# emp = Employee()
# dev = Developer()
# man = Manager()

# emp.work()
# dev.work()
# man.work()

# import pygame

# pygame.init()
# screen = pygame.display.set_mode((600, 400))

# class GameObject:
#     def draw(self):
#         pass

# class Player(GameObject):
#     def draw(self):
#         pygame.draw.circle(screen, "blue", (100, 200), 30)

# class Enemy(GameObject):
#     def draw(self):
#         pygame.draw.rect(screen, "red", (250, 170, 60, 60))

# class Coin(GameObject):
#     def draw(self):
#         pygame.draw.circle(screen, "yellow", (450, 200), 20)

# objects = [Player(), Enemy(), Coin()]
# running = True

# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     screen.fill("white")

#     for obj in objects:
#         obj.draw() # Same method, different behavior

#     pygame.display.update()

# pygame.quit()


# # ENCAPSULATION
# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.__balance = balance      # Private variable

#     def deposit(self, amount):
#         self.__balance += amount

#     def withdraw(self, amount):
#         if amount <= self.__balance:
#             self.__balance -= amount
#         else:
#             print("Insufficient Balance")

#     def show_balance(self):
#         print("Balance:", self.__balance)


# acc = BankAccount("Dhruv", 5000)

# acc.show_balance()

# acc.deposit(2000)
# acc.show_balance()

# acc.withdraw(3000)
# acc.show_balance()

# ## This will give an error
# # print(acc.__balance)


# # COMBINED CODE
# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.__salary = salary      # Encapsulation

#     def work(self):                 # Polymorphism
#         print(self.name, "is working.")

#     def show_salary(self):
#         print("Salary:", self.__salary)


# class Developer(Employee):          # Inheritance
#     def work(self):
#         print(self.name, "is coding in Python.")


# class Manager(Employee):
#     def work(self):
#         print(self.name, "is managing the project.")


# dev = Developer("Alice", 70000)
# man = Manager("Bob", 90000)

# employees = [dev, man]

# for emp in employees:
#     emp.work()          # Polymorphism
#     emp.show_salary()   # Encapsulation

import pygame

pygame.init()

screen = pygame.display.set_mode((500, 400))
clock = pygame.time.Clock()

class Ball:
    def __init__(self, x):
        self.x = x

    def move(self):
        pass

    def draw(self):
        pygame.draw.circle(screen, "white", (self.x, 200), 20)

class FastBall(Ball):
    def move(self):
        self.x += 5

class SlowBall(Ball):
    def move(self):
        self.x += 2

balls = [FastBall(50), SlowBall(50)]

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    for ball in balls:
        ball.move() # Polymorphism
        ball.draw()

    pygame.display.update()
    clock.tick(60)

pygame.quit()
