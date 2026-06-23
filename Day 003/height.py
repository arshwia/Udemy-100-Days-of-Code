height = int(input("How tall are you(cm)? "))
price = 0

if height >= 120:
    age = int(input("pls enter your age: "))
    if age <= 18:
        price = 7
        print(f"You can ride it and it costs ${price}.")

        photo = input("Do you want a photo, $3 will be added to the price.(Yes or no)?")

        if photo == "Yes":
            price = price + 3
            print(f"You can ride it and it costs ${price}")
        else:
            print(f"You can ride it and it costs ${price}")
    else:
        price = 18
        print(f"You can ride it and it costs ${price}.")

        photo = input("Do you want a photo, $3 will be added to the price.(Yes or no)?")

        if photo == "Yes":
            price = price + 3
            print(f"You can ride it and it costs ${price}")
        else:
            print(f"You can ride it and it costs ${price}")
else:
    print("I'm sorry, you can't ride.")
