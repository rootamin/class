first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = input("Enter your age: ")
weight = input("Enter your weight: ")
height = input("Enter your height: ")

bmi = int(weight) / int(height) ** 2

bmi = round(bmi, 5)

# this prints the final result.
print(f"Hi {first_name} {last_name}. You are {age}. Your bmi is {bmi}")