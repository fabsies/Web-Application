class Fruits():
    def __init__(self,name,price,colour):
        self.name = name
        self.price = price
        self.colour= colour
    def display(self):
        print('My favourite fruit is',self.name, 'it is priced at',self.price, 'shillings and it is', self.colour,'in colour')
f1 = Fruits('Banana',10, 'yellow')
f2 = Fruits('Apple', 35, 'Red')
f3 = Fruits('Orange', 15, 'Orange')
f4 = Fruits('Grapes', 250, 'Purple')
f5 = Fruits('Dragonfruit', 150, 'Pink')
f1.display()
f2.display()
f3.display()
f4.display()
f5.display()