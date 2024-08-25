# a simple calculator
first_number = float(input("First number: "))
second_number = float(input("Second number: "))

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
    exit()   # This is not necessary but it would exit our code without showing the error.

print(f"{first_number} {operation_mode} {second_number} = {result}")