# ## WRITE OPERATIONS
# hero = input("Enter your first superhero: ")

# file = open("superheroes.txt", "w")
# file.write(hero)
# file.close()

# print("First superhero added!")

# # ## APPEND OPERATIONS
hero = input("Enter another superhero: ")

file = open("superheroes.txt", "a")
file.write("\n" + hero)
file.close()

print("Superhero added to the team!")

# # ## READ OPERATIONS
# file = open("superheroes.txt", "r")

# print("\nMy Superhero Team")
# print(file.read())

# file.close()

# n = open('trial.txt', mode = 'r')
# x = n.readlines()
# print(x)
# n.close()