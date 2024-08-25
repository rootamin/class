def reverse_kon(text):
    text = text.lower().replace(" ", "")
    return text == text[::-1]

text = input("Enter your word: ")

if reverse_kon(text):
    print("It's reverse is equal.")
