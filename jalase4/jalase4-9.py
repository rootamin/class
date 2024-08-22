# dictionaries

my_dict = {
    "name": "Salimi",
    "age": 18, 
    "city": "Zanjan"
}

# gets the absolute value
print(my_dict["city"])

# gets the optional value
print(my_dict.get("name", "Not found"))


my_dict["email"] = "salimi@gmail.com"
del my_dict["name"]


print(my_dict)