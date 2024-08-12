# a simple, running calculator
while True:
    first_number = int(input("First number: "))
    second_number = int(input("Second number: "))

    operation_mode = input("What operation do you want? (+ - x %): ")

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

    print(f"{first_number} {operation_mode} {second_number} = {result}")
    want_out = input("Do you wanna do another operation? (y or n) ")
    print('\n===================')

    if want_out == "n":
        break