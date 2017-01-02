#Temperature converter
Job= "0"
#Loop until "3" in Job
while "3" not in Job:
    Job= input("Select 1. Celsius to Fahrenheit, 2.Fahrenheit to Celsius, 3. To exit")
    if "1" in Job:
        #Celcius to Fahrenheit
        temp= float(input("Please type in the temperature"))
        newTemp= ((temp*(9/5)+32))
        print(newTemp,"°F")
                    
    if "2" in Job:
        #Fahrenheit to Celcius
        temp= float(input("Please type in the temperature"))
        newTemp= ((temp - 32)*(5/9))
        print(newTemp, "°C")
                    
    
                    
