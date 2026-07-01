import random

friends = ["arshia", "MAMAD", "mahi", "hadis"]

number_of_friends = len(friends)
random_number = random.randint(0, number_of_friends - 1)

print(friends[random_number])
