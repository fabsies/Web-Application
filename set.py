my_set = {112, 244, 456, 902, 567, 984}
print(my_set)
char = 112
if char in my_set:
    output = char
    print(output)
my_set.add(242)
print(my_set)
my_set.update([121, 2323, 242])
print(my_set)
my_set2 = my_set.copy()
print(my_set2)
print(len(my_set2))
my_set2.discard(121)
print(my_set2)
del my_set
print(my_set2)
max(my_set2)
print(max(my_set2))
min(my_set2)
print(min(my_set2))
sum(my_set2)
print(sum(my_set2))
