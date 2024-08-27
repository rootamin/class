import os


if os.path.exists("example.txt"):
    print("File exists.")
    os.remove("example.txt")

else:
    print("File does not exist.")