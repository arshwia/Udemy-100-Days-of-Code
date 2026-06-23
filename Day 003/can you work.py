did_you_eat = input("did you eat? (True of False)")

if did_you_eat == "True":
    drink_coffee = input("did you coffee? (True of False)")

    if drink_coffee == "True":
        print("You can work!")
    else:
        print("You can't work!")
        print("Because you didn't drink coffee.")
else:
    print("You can't work!")
    print("Because you didn't eat.")
