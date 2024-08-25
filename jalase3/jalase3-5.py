# a simple, running calculator
def calculator():
    while True:


        result = "empty"
        while True:
            if result == "empty":
                first_number = int(input("First number: "))
                operation_mode = input("What operation do you want? (+ - x %): ")
                second_number = int(input("Second number: "))

                if operation_mode == "+":
                    result = first_number + second_number
                elif operation_mode == "-":
                    result = first_number - second_number
                elif operation_mode == "x":
                    result = first_number * second_number
                elif operation_mode == "%":
                    result = first_number / second_number

                else:
                    print("Invalid operation.")
                    exit()

                print(f"result = {result}")

            else:
                operation_mode = input("What operation do you want? (+ - x % =): ")
                if operation_mode == "=":
                    print(f"result = {result}")
                    break

                number = int(input("Next Number: "))

                if operation_mode == "+":
                    result = result + number
                elif operation_mode == "-":
                    result = result - number
                elif operation_mode == "x":
                    result = result * number
                elif operation_mode == "%":
                    result = result / number

                else:
                    print("Invalid operation.")
                    exit()

                print(f"result = {result}")

        
        want_out = input("Do you wanna do another operation? (y or n) ")
        print('\n===================')

        if want_out == "n":
            break


# Simple BMI calculator
def bmi_calculator():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    age = input("Enter your age: ")
    weight = input("Enter your weight: ")
    height = input("Enter your height: ")

    bmi = int(weight) / (int(height) / 100) ** 2

    bmi = round(bmi, 5)

    # this prints the final result.
    print(f"Hi {first_name} {last_name}. You are {age}. Your bmi is {bmi}")



while True:
    print("Hi.\n Do you wanna use calculator or bmi_calculator?")
    choice = input("Choose (c/b/e): ")

    if choice == "c":
        calculator()
    elif choice == "b":
        bmi_calculator()
    elif choice == "e":
        print("Goodbye")
        exit()

    else:
        print("Invalid Choice.")