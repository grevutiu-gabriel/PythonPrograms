#BMI calculator
weight= 0
height= 0
BMI= 0
#weight calculation

weightUnit= str(input("What do you know your weight in?"))
weight= float(input("What is your weight"))

#converting weight to kg
if weightUnit.lower()== "kg" or "kilograms":
    weight= weight
elif weightUnit.lower()== "stone" or "st":
    weight= weight*6.35029318
else:
    print("I'm sorry that unit is not supported")

#Height calculation
heightUnit= str(input("What do you know your height in?"))
height= float(input("What is your height?"))

#converting height to m
if heightUnit.lower()== "m" or "metres":
    height= height
elif heightUnit.lower()== "feet" or "foot" or "ft":
    height= height/0.3048
else:
    print("I'm sorry that unit is not supported")

BMI= int((weight)/(height)/(height))
print(BMI)

if BMI<18.5:
    print("You are underweight")
elif BMI >=18.5 and BMI <=24.9:
    print("You are normal weight")
elif BMI >=25 and BMI <=29.9:
    print("you are overweight")
else:
    print("you are obese")
