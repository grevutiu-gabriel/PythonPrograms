#Big Number Generator
##################################################################
##################################################################
def BigNumberGen(UserNumber):
    #NumberArray
    BigNumbers = [
    ["*******","*     *","*     *","*     *","*     *","*     *","*******"],
    ["    ***","   *  *"," *    *","      *","      *","      *","*******"],
    ["*****  ","     **","    ** ","   **  ","  **   "," **    ","*******"],
    ["*******","      *","      *","*******","      *","      *","*******"],
    ["*     *","*     *","*     *","*******","      *","      *","      *"],
    ["*******","*      ","*      ","*******","      *","      *","*******"],
    ["*******","*      ","*      ","*******","*     *","*     *","*******"],
    ["*******","      *","      *","      *","      *","      *","      *"],
    ["*******","*     *","*     *","*******","*     *","*     *","*******"],
    ["*******","*     *","*     *","*******","      *","      *","*******"]]

    #Printing out a number
    #Empty array for amalgamating number parts
    FinalNumber= []
    
    #Range 0,7 as that is the number of components per number
    for x in range (0,7):
        #Puts first line of each number into new array (in required order) e.g 6,0 5,0 6,1 5,1
        for i in range (0,len(UserNumber)):
            FinalNumber.append(BigNumbers[int(UserNumber[i])][x])
            FinalNumber.append("     ")
                
        FinalNumber.append("\n")
        
    print("\n\n")
    #Joining and printing final number
    print(''.join(FinalNumber),"     ")

##################################################################
##################################################################
UserNumber = input("What number would you like?")
if len(UserNumber) > 6:
    print("sorry that number has too many digits")
else:
    BigNumberGen(UserNumber)

