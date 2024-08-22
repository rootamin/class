#using for loops in dictionaries
my_dict = {"name": "Vahid", 'age': 18, 'city': 'Zanjan', 'email': 'salimi@gmail.com'} 

for key in my_dict:
    print(key, my_dict[key])


for key, value in my_dict.items():
    print(key, value)