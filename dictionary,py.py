my_dictionary = {
    "Name": "Fabiola",
    "Gender": "Female",
    "School": "School of Engineering"
}

my_dictionary = dict(
    Name="Fabiola",
    Gender="Female",
    School="School of Engineering"
)
print(my_dictionary)
print(my_dictionary['Name'])
print(my_dictionary['Gender'])
my_dictionary['Gender'] = 'Male'
print(my_dictionary)
my_dictionary['Age'] = 18
print(my_dictionary)
my_dictionary2 = my_dictionary.copy()
print(my_dictionary2)
print(len(my_dictionary2))
my_dictionary2.pop('Gender') #removes the gender
print(my_dictionary2)
del my_dictionary
for value in my_dictionary2:
    print(my_dictionary2[value])  #prints dict values
for key in my_dictionary2:
    print(key)   #prints dict keys

