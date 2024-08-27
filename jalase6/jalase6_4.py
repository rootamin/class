# Writing a file


file = open("example2.txt", "w") # a for appending

# Writing
file.write("Hello, World!\n")


# bulk writing using list
lines = ["Line1\n", "Line2\n", "Line3\n"]
file.writelines(lines)


file.close()