import random

data = {
    0: """    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
    1: """    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
""",
    2: """    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""",
}


def win_or_lose(user_choice, pc_choice):
    if user_choice not in data:
        print("Invalid choice.")
        exit()

    print(f"your choice\n{data[user_choice]}")
    print(f"pc choice\n{data[pc_choice]}\n\n")

    if (
        (user_choice == 0 and pc_choice == 2)
        or (user_choice == 1 and pc_choice == 0)
        or (user_choice == 2 and pc_choice == 1)
    ):
        print("win")
    elif user_choice == pc_choice:
        print("equal")
    else:
        print("lose")


pc_choice = random.randint(0, 2)
user_choice = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
)

win_or_lose(user_choice, pc_choice)
