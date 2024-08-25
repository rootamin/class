# formatting strings, f strings and more.
name = "MirMatin"
age = 6

greetings = f"My name is {name} and I'm {age} years old."
greetings = "My name is {} and I'm {} years old.".format(name, age)
greetings = "My name is %s and I'm %s years old." % (name, age)

print(greetings)