# Binary example

with open("image.png", "rb") as img_file:
    data = img_file.read()


with open("copy_image.png", "wb") as img_copy:
    img_copy.write(data)