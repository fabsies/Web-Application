my_tuple = (123, 232, 332, 454, 545, 'Fabsies')
print(my_tuple)
print(my_tuple[2])
print(my_tuple[2:5])
print(len(my_tuple))
del my_tuple

my_tuple2 = (123, 232, 332, 454, 322)
if 'cooking' in my_tuple2:
    print('Yes, cooking is present')
else:
    print('No, cooking found')
print(max(my_tuple2))
print(min(my_tuple2))
print(sum(my_tuple2))
print(my_tuple2.count(332))
print(sum(my_tuple2)/len(my_tuple2))