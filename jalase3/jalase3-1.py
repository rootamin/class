# a simple, running calculator
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