print("Welcome to the tip calculator!")

invoice = float(input("What was total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

tip_mony = invoice * tip / 100
all_mony = invoice + tip_mony

each_person = all_mony / people

print(f"Each person should pay: ${round(each_person, 2)}")
