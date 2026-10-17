# # Create and Print a Tuple
# ucl_teams = ("Real Madrid", "Barcelona", "Bayern Munich")

# print(ucl_teams)


# # Access Tuple Elements
# goals = (1, 2, 3, 4, 5)

# print("First Goal Count:", goals[0])
# print("Last Goal Count:", goals[-1])


# # Find Length of a Tuple
# clubs = ("Real Madrid", "Manchester City", "PSG", "Inter Milan")

# print("Number of Clubs:", len(clubs))


# # Count Occurrences
# results = ("Win", "Draw", "Win", "Loss", "Win")

# print(results.count("Win"))


# # Find Index of an Element
# ucl_teams = ("Real Madrid", "Barcelona", "Bayern Munich")

# print(ucl_teams.index("Barcelona"))


# # Iterate Through a Tuple
# players = ("Mbappe", "Haaland", "Bellingham")

# for i in players:
#     print(i)


# # Tuple Packing and Unpacking
# player = ("Bellingham", 22, "Real Madrid")
# name, age, club = player

# print(name)
# print(age)
# print(club)


# # Concatenate Tuples
# group_a = ("Real Madrid", "PSG", "Arsenal")
# group_b = ("Bayern Munich", "Inter Milan", "Barcelona")

# all_teams = group_a + group_b

# print(all_teams)


# # Create and Print a Dictionary
# player_info = {
#     "Name": "Mbappe",
#     "Age": 27,
#     "Club": "Real Madrid"
# }

# print(player_info)


# # Access Dictionary Values
# player_info = {
#     "Name": "Mbappe",
#     "Age": 27,
#     "Club": "Real Madrid"
# }

# print(player_info["Name"])
# print(player_info["Club"])


# # Add a New Key-Value Pair
# player_info = {
#     "Name": "Mbappe",
#     "Age": 27
# }

# player_info["Position"] = "Forward"

# print(player_info)


# Update a Value
# player_info = {
#     "Name": "Mbappe",
#     "Age": 27
# }

# player_info["Age"] = 28

# print(player_info)


# # Delete an Element
# player_info = {
#     "Name": "Mbappe",
#     "Age": 27,
#     "Club": "Real Madrid"
# }

# del player_info["Club"]

# print(player_info)


# # Iterate Through Dictionary
player_info = {
    "Name": "Mbappe",
    "Age": 27,
    "Club": "Real Madrid"
}

for key, value in player_info.items():
    print(key, ":", value)


# # Print Only Keys
# player_info = {
#     "Name": "Mbappe",
#     "Age": 27,
#     "Club": "Real Madrid"
# }

for key in player_info.keys():
    print(key)


# # Print Only Values
# player_info = {
#     "Name": "Mbappe",
#     "Age": 27,
#     "Club": "Real Madrid"
# }

for value in player_info.values():
    print(value)