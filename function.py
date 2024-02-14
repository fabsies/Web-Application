print("This is my first function")
print("This is my first function")
print("This is my first function")
def my_function():
    text = "This is my first function"
    print(text)
    print(text)
    print(text)
my_function()

def number_one():
    number = input("Enter a number: ")
    print(number)
number_one()

def num_two(text):
   print(text)
   print(text)
   print(text)
num_two("This is my first class")

def student_name(firstname, lastname):
    print(firstname + lastname )
student_name("Felix","Kegode")

def author_details(firstname, lastname):
    print(firstname + " " + lastname + " " + "Goodmorning")
author_details("leigh", "Bardugo")
author_details("Cassie", "Leeza")
author_details("John", "Doe")

# def school_age(firstname,age):
#     if age < 10:
#         print(firstname + "You are young")
#     elif age > 10:
#         print(firstname + "You are middle aged")
#     else:
#         print(firstname + "You are older")
# school_age("Tricia","9")
# school_age("James", "18")
# school_age("Donna", "45")

def add_age(age):
    new_age = age + 10
    return new_age
future_age = add_age(20)
print(future_age)

def subtract_age(age):
    old_age = age + 18
    return old_age
previous_age = subtract_age(-15)
print(previous_age)

def performance(english, math):
    total = english + math
    return total
print(performance(34,45))

def performance1(*marks):
    total = sum(marks)
    return total
print(performance1(23,45,656))
print(performance1(34,78,56,67))
print(performance1(97,58,59,55,39,60,78))
print(performance1(456))
print(performance1(12,67,98,45))

def country(nchi = 'Kenya'):
    return nchi
print(country('Norway'))
print(country('China'))
print(country('Switzerland'))
print(country())