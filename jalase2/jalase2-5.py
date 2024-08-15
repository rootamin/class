"""
for i in range(3):
    print(i)

for i in range(20, 100, 7):
    print(i)


letters = "python"

for letter in letters:
    print(letter)
"""

x = 0
for i in range(4):
    x = x + 1
    print(f"asli : {x}")

    y = 0
    for j in range(10):
        y = y + 1
        print(y)

"""
    for j in range(2):
        x = x + 1
        print(f"farei: {x}")
       # print(f"this is j = {j}")
"""


x = 0
while True:
    x = x + 1

    print(x)


count = 1
while count < 5:
    print(count)
    count += 1


count = 0
state = True
while state:
    count += 1
    print(count)

    if count == 2000:
        break
        # or
        # state = False

while True:
    print("this will run forever")
