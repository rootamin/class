# file handling

file_object = open("filename", "<mode>")

"""
Types of modes:

r : Read (default), Just for reading, Raises and error file doesn't exist
w : Write, Opens the file, If the file exists, it resets it, If it's not, it will create a new file
a : Append, Appends in a new line regardless of previous contents, If the file dosn't exist, it creates it.
b : Binary mode, handle binary files like images, videos, etc.
"""

# close the file:
file_object.close()