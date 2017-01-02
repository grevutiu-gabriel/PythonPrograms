#Defining the procedure
def squarep(myNumber):
    result = myNumber * myNumber
    print("The square of ", myNumber, " is", result)

myNumber = int(input("What number?"))
squarep(myNumber)



#Defining the Function
def squaref(myNumber):
    result = myNumber * myNumber
    return result

myNumber = int(input("What number?"))
print(squaref(myNumber))
