import random

alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
numbers = [
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]


def main(nr_letters, nr_symbols, nr_numbers):
    # nr_letters
    random_letter = ""

    for _ in alphabet:
        random_letter += random.choice(alphabet)
        if nr_letters == len(random_letter):
            break

    random_number = ""

    for _ in numbers:
        random_number += random.choice(numbers)
        if nr_symbols == len(random_number):
            break

    random_symbile = ""

    for _ in symbols:
        random_symbile += random.choice(symbols)
        if nr_numbers == len(random_symbile):
            break

    print(random_letter, random_number, random_symbile)

    password = random_letter + random_number + random_symbile

    password = list(password)
    random.shuffle(password)

    password = "".join(password)

    print(password)


print("Welcome to the PyPassword Generator!")

nr_letters = int(input("How many letters would you like in your password?"))
nr_symbols = int(input("How many symbols would you like?"))
nr_numbers = int(input("How many numbers would you like?"))

main(nr_letters, nr_symbols, nr_numbers)
