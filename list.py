my_list = [345, 553, 21, 54, 56, 67, 65, 67]
print(my_list)
print(my_list[2])
print(my_list[7])
print(my_list[3:7])
my_list[1] = 520
print(my_list)
my_list[5] = 94
print(my_list)
my_list.append(73)
print(my_list)
my_list.insert(3,50)
print(my_list)
my_list.extend([456, 567, 678])
print(my_list)
my_list.remove(65)
print(my_list)
del my_list[2]
print(my_list)
my_list.clear()
print(my_list)
my_list.extend([12, 13, 14, 15, 16, 17, 18, 19, 20])
print(my_list)
del my_list
my_list2 = [313, 543, 767, 7888, 9875]
print(my_list2)
my_list2.append(535)
print(my_list2)
if 18 in my_list2:
    print('The Value is in the list')
else:
    print('The Value is not found')
my_list3 = (313, 543, 767, 313, 5464, 34234, 313, 514)
print(my_list3.count(3130))
print(max(my_list3))
print(min(my_list3))
print(sum(my_list3))
print(len(my_list3))
print(my_list3.index(34234))

my_list4 = ['tree', 'trunk', 'stems', 'flowers', 'leaves']
print(my_list4)
my_list4.extend(['wood', 'twigs'])
print(my_list4)
if 'stems' in my_list4:
    print('The value is in my list')
else:
    print('Value not found')
my_list4.extend([54,89,67])
print(my_list4)
