height = int(input("How tall are you(cm)? "))

if height >= 120:
    age = int(input("pls enter your age: "))
    if age <= 18:
        print("You can ride it and it costs $7.")
    else:
        print("You can ride it and it costs $18.")
else:
    print("I'm sorry, you can't ride.")
