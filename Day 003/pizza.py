print("Welcome to Python pizza")

size = input("What size pizza do you want? S, M or L: ")

price = 0

# small pizza (S) = $15
if size == "S":
    price = price + 15

    pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
    if pepperoni == "Y":
        price = price + 2

    extra_cheese = input("Do you want extra cheese? Y, N: ")
    if extra_cheese == "Y":
        price = price + 1

    print(f"your pizza price : {price}")

elif size == "M":
    price = price + 20

    pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
    if pepperoni == "Y":
        price = price + 3

    extra_cheese = input("Do you want extra cheese? Y, N: ")
    if extra_cheese == "Y":
        price = price + 1

    print(f"your pizza price : {price}")

elif size == "L":
    price = price + 25

    pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
    if pepperoni == "Y":
        price = price + 3

    extra_cheese = input("Do you want extra cheese? Y, N: ")
    if extra_cheese == "Y":
        price = price + 1

    print(f"your pizza price : {price}")
