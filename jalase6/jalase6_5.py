# using with statement to open files.

with open("example2.txt", "w") as file:
    content = file.read()
    
    print(content)