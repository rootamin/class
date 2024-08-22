# Sets, Union, intersection, difference in sets
my_set1 = {1, 6, 3, 2}
my_set2 = {4, 3, 5, 6}



print(my_set1.union(my_set2))
print(my_set1.intersection(my_set2))
print(my_set1.difference(my_set2))

print(my_set2.difference(my_set1))

print(my_set1.symmetric_difference(my_set2))
