print("Welcome to the tip calculator!")

bill = float(input("What was total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

tip_mony = bill * tip / 100
bill_with_tip = bill + tip_mony

each_person = bill_with_tip / people

print(f"Each person should pay: ${round(each_person, 2)}")
