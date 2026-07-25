def add(number1, number2):
    return number1 + number2


def subtract(number1, number2):
    return number1 - number2


def multiply(number1, number2):
    return number1 * number2


def divide(number1, number2):
    return number1 / number2


number1 = 2
number2 = 3

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    should_accumulate = True

    num1 = float(input("What is the fitst number? "))

    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operation_symbol = str(input("pick an operation: "))

        num2 = float(input("What is the next number? "))

        answar = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answar}")

        choice = str(
            input(
                f"Type 'y' to continue calculating with {answar}, or type 'n' to start a new calculation: "
            )
        ).lower()

        if choice == "y":
            num1 = answar
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()


calculator()
