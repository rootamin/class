"""
def get_name_and_age():
    name = "Salimi"
    age = 18
    return name, age

name = "Amin"
print(name)

person_name, person_age = get_name_and_age()

print(f"Hi, I'm {person_name} and I'm {person_age}")
"""

y = 20
def my_func():
    global y
    y = 18


my_func()
print(y)