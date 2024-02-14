class Details():
     def __init__(self, first_name, last_name, age, gender):
         self.first_name = first_name
         self.last_name = last_name
         self.age = age
         self.gender = gender

     def display(self):
         print('My name is', self.first_name + ' ' + self.last_name, ', I am', self.age, 'years old' ' and I am', self.gender)
d1 = Details('John','Doe',34, 'Male')
d2 = Details('Ana', 'Karenina', 21, 'Female')
d3 = Details('Ellie','Smith', 20, 'Female')
d4 = Details('Ted','Finn', 57, 'Male')
d1.display()
d2.display()
d3.display()
d4.display()



