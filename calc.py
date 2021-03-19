def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculation():

    num1 = int(input("What is the first number  ? : "))

    for symbol in operations:
        print(symbol)

    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation from the line above : ")
        num2 = int(input("What is the next number  ? : "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1}{operation_symbol}{num2} = {answer}")

        if input(f"type 'y' to continue calculating with {answer} , or type 'n' to start a new calculation :") == 'y':
            num1 = answer
        else:
            should_continue = False
            calculation()
            print("Good Bye!!")


calculation()
# operation_symbol = input("Pick another operation : ")
# num3 = int(input("What is the next number  ? : "))
# calculation_function = operations[operation_symbol]
# second_answer = calculation_function(first_answer, num3)

# print(f"{first_answer}{operation_symbol}{num3} = {second_answer}")

# type 'y' to continue calculating with 16 , or type 'n' to exit :
