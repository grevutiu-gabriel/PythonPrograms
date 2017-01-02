import random

dividable_numbers = random.randint(1,999999999999999999999999999999999999999999999999999999999999)

loop = True
dividable = False

while loop == True:
    number = random.randint(1,999999999999999999999999999999999999999999999999)
    if (number % dividable_numbers) == 1:
        loop = False

    else:
        loop = True
        print("yes")
        
