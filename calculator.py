print("******* CALCULATOR *******")
def calc():
    number1 = int(input("enter your first number: "))
    number2 = int(input("enter your second number: "))
    operator = input ("Do you want to +, -, x or /?")

    if operator == "+":
        answer = number1 + number2

    elif operator == "-":
        answer = number1 - number2

    elif operator == "x":
        answer = number1 * number2

    elif operator == "/":
        answer = number1 / number2

    else:
        print("Invalid input")
        calc()
    print ("The answer = " + str(answer))

calc()
