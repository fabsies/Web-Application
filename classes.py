# class Person:
#     age = 32
#     print(age)
# p1 = Person()
# print(p1.age)

# class Student():
#     Grade = 'A'
#     print(Grade)
# student1 = Student()
# print(student1.Grade)

# class Employees():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# Employee1 = Employees('Alex', 36)
# Employee2 = Employees('Doreen', 45)
# Employee3 = Employees('Joan', 27)
# print(Employee1)
# print(Employee2)
# print(Employee3)
class Students():
    def __init__ (self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def display(self):
       print('My name is', (self.name))
       print('My age is', (self.age))
       print('My marks are', (self.marks))

s1 = Students('John', 34, 234)
s1.display()
s2 = Students('Kacy', 76, 333)
s2.display()

