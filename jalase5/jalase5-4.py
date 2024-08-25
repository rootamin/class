# finding, splitting, joining and replacing strings.

word = "hello world! python. salim% matin&"

print(word.find("r"))

word = word.replace("!", "")
word = word.replace(".", "")
word = word.replace("%", "")
word = word.replace("&", "")

word = word.split(" ")


word = ".".join(word)
print(word)