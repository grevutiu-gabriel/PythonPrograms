#Universal converter
jobType= "0"
while "5" not in jobType:
    jobType= input("What type of conversion? 1: Length, 2:Weight, 3:Temperature, 4:Speed, 5:Exit")

    #Length
    if "1" in jobType:
        job= input("What would you like converted? 1: cm to inches, 2: inches to cm, 3: m to feet, 4: feet to m, 5: Return to previous menu")
        if "1" in job:
            #cm to inches
            oriNumber= float(input("What number would you like converted?"))
            newNumber= (oriNumber/2.54)
            print(newNumber)
        if "2" in job:
            #inches to cm
            oriNumber= float(input("What number would you like converted?"))
            newNumber= (oriNumber*2.54)
            print(newNumber)
        if "3" in job:
            #m to feet
            oriNumber= float(input("What number would you like converted?"))
            newNumber= (oriNumber*3.28084)
            print(newNumber)
        if "4" in job:
            #feet to m
            oriNumber= float(input("What number would you like converted?"))
            newNumber= (oriNumber/3.28084)
            print(newNumber)
        jobtype= "0"

    #Weight
    if "2" in jobType:
        job= input("What would you like converted? 1:Grams to Pounds, 2:Pounds to Grams, 3:Kilogram to Stone, 4: Stone to Kilogram, 5:Return to previous menu")
        if "1" in job:
            #Grams to Pounds
            oriNumber= float(input("What number would you like converted?"))
            newNumber= (oriNumber/0.00220462)
            print(newNumber)
        if "2" in job:
            #Pounds to Grams
            oriNumber= float(input("What number would you like converted?"))
            newNumber= (oriNumber*0.00220462)
            print(newNumber)
        if "3" in job:
            #Kilogram to stone
            oriNumber= float(input("What number would you like converted?"))
            newNumber= (oriNumber/0.157473)
            print(newNumber)
        if "4" in job:
            #Stone to Kilogram
            oriNumber= float(input("What number would you like converted?"))
            newNumber= (oriNumber*0.157473)
            print(newNumber)
        jobtype= "0"
            
    if "3" in jobType:
        Job= input("What would you like converted? 1. Celsius to Fahrenheit, 2.Fahrenheit to Celsius, 3. Return to previous menu")
        if "1" in Job:
            #Celcius to Fahrenheit
            oriNumber= float(input("Please type in the temperature"))
            newNumber= ((temp*(9/5)+32))
            print(newNumber,"°F")
                        
        if "2" in Job:
            #Fahrenheit to Celcius
            oriNumber= float(input("Please type in the temperature"))
            newNumber= ((temp - 32)*(5/9))
            print(newNumber, "°C")
        jobtype= "0"
            
    if "4" in jobType:
        Job= input("What would you like converted? 1.Kph to Mph, 2.Mph to Kph, 3. Return to previous menu")
        if "1" in Job:
            #Kph to Mph
            oriNumber= float(input("What number would you like converted?"))
            newNumber= (oriNumber/0.621371)
            print(newNumber)
        if "2" in Job:
            #Mph to Kph
            oriNumber= float(input("What number would you like converted?"))
            newNumber= (oriNumber*0.621371)
            print(newNumber)
        jobtype= "0"

            
        
                    
        
        
            
