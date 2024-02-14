my_list = [1,2,3,4,5,6,7,8,9]
print(my_list)
total = 0
for num in my_list:
    total += num
print(total, "is your output")
maths = float(input("Enter maths score "))
range = float(1 -100)
english = float(input("Enter english score "))
range = float(1 - 100)
print(maths, english)
if maths < 30 or english < 30:
    print("You have failed")
else:
    print("You have passed")

