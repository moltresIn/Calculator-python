def calculator(firstNumber: int, secondNumber: int, operation: int):
    if operation == 1:
        print("The First number is ", firstNumber, "\nThe second number is ", secondNumber, "\nThe value of "
                                                                                            "adding two is ",
              firstNumber + secondNumber)
    if operation == 2:
        print("The First number is ", firstNumber, "\nThe second number is ", secondNumber, "\nThe value of "
                                                                                            "subtracting two is ",
              firstNumber - secondNumber)
    if operation == 3:
        print("The First number is ", firstNumber, "\nThe second number is ", secondNumber, "\nThe value of "
                                                                                            "multiplying two is ",
              firstNumber * secondNumber)
    if operation == 4:
        print("The First number is ", firstNumber, "\nThe second number is ", secondNumber, "\nThe value of "
                                                                                            "dividing two is ",
              firstNumber / secondNumber)


if __name__ == '__main__':
    num1 = int(input("Enter The First number >> "))
    num2 = int(input("Enter The Second number >> "))
    print("Choose the option below:\n 1. Addition \n 2. Subtraction \n 3. Multiplication \n 4. Division \n")
    action = int(input("Enter the option >> "))
    calculator(num1, num2, action)