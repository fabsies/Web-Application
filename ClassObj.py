class Employees:
    raise_amt = 1.05
    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = first_name + '.' + last_name + '@gmail.com'
    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)
    def apply_raise(self):
         self.pay = float(self.pay * self.raise_amt)
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount
class Developer(Employees):
    def __init__(self, first_name, last_name, pay, language):
        super().__init__(first_name, last_name, pay)
        self.language = language
class Watchman(Employees):
    def __init__(self, first_name, last_name, pay, Gender):
        super().__init__(first_name, last_name, pay)
        self.Gender = Gender

emp1 = Employees("Jesper", "Fahey", 13000)
emp2 = Employees("Zoya", "Nazyalensky", 9000 )
print(emp1.first_name)
print(emp2.first_name)
print(emp1.email)
print(emp2.email)
print(f"{emp1.first_name} {emp1.last_name} salary is {emp1.pay}")
print(f"{emp2.first_name} {emp2.last_name} salary is {emp2.pay}")
print(emp1.full_name())
print(emp2.full_name())
print(emp1.pay)
emp1.apply_raise()
print(emp1.pay)
Employees.raise_amt = 2.05
print(Employees.raise_amt)
print(emp1.pay)
emp1.apply_raise()
print(emp1.pay)
Employees.set_raise_amt(1.05)
print(Employees.raise_amt)
print(emp1.pay)
emp1.apply_raise()
print(emp1.pay)
dev1 = Developer("David", "Kostyk", 45000, "Julia")
dev2 = Developer("Genya", "Safin", 56000, "Ethereum" )
print(dev1.language)
print(dev2.language)
wm1 = Watchman("Jarl", "Brum", 10000, "Male")
wm2 = Watchman("Hanne", "Brumm", 2400, "Female")
print(wm1.first_name, wm1.Gender)
print(wm2.first_name, wm2.Gender)



