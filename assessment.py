weight = float(input("Please enter your weight"))
height = float(input("Please enter your height "))
print(weight)
print(height)
BMI = float(weight)/float(height)**2
print(BMI)
if BMI < 18:
    print("You are underweight")
elif BMI <= 24:
    print("Your weight is normal")
elif BMI <= 30:
    print("You are overweight")
else:
    print("You are obese")
