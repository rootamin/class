# a simple, running calculator, with infinite number inputs
while True:

    result = "empty"
    while True:
        if result == "empty":  # determines whether the calculator has been used or not.
            first_number = float(input("First number: "))
            operation_mode = input("What operation do you want? (+ - x %): ") # we don't have = because it's the first time we are running the calculator.
            second_number = float(input("Second number: "))

            if operation_mode == "+": # same principals from the first step.
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

        else:  # runs when the calculator is used. Because if it's used, we are guaranteed to have a non-string result variable. 
            operation_mode = input("What operation do you want? (+ - x % =): ")
            if operation_mode == "=":  # we wanna close our loop when the input is =.
                print(f"result = {result}")
                break

            number = float(input("Next Number: ")) # only one number since there is a previous result stored.

            if operation_mode == "+": 
                result = result + number # instead of first number and second number, we are operating on our previously stored result and our new number in this condition.
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

    
    want_out = input("Do you wanna do another operation? (y or n) ") # same principals from the 2nd step.

    if want_out == "n":
        break