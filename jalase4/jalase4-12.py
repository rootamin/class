# creating a key value automatically in python
x = 0
first_list = []
for i in range(10):
    x += 1
    first_list.append("var" + str(x))

print(first_list)


y = 0
second_list = []
for j in range(10):
    y += 10
    second_list.append(y)

print(second_list)

final_dict = {}

for item1, item2 in zip(first_list, second_list):
    final_dict[item1] = item2


print(final_dict)