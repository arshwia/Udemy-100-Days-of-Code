import random

random_number = random.randint(1, 10)
print(random_number)
if random_number < 5:
    print("heads")
elif random_number == 5:
    print("body xD")
else:
    print("tails")
