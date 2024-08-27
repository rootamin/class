# opening file example
file = open("example.txt", "r")

# Reads the whole file read()
# content = file.read()


# Reads the first line readline()
# content = file.readline()


# Reads line by line and returns a list
content = file.readlines()
print(content)


file.close()