#Siteswap checker
#############################################################################
def SiteSwapCheck(Num1,Num2,Num3):
    Allowed = True
    #Rule 1 (If divisible by 3)
    if not ((Num1 + Num2 + Num3)%3) == 0:
        Allowed = False

    #Rule 2 (no number after previous equal to one less than previous)
    if Num1 == (Num2 + 1):  
        Allowed = False

    if Num2 == (Num3 + 1):  
        Allowed = False

    if Num3 == (Num1 + 1):  
        Allowed = False

    if Allowed == False:
        return("INVALID SITESWAP")
############################################################################
try:         
    Num1 = int(input("Please input the first number"))
    Num2 = int(input("Please input the second number"))
    Num3 = int(input("Please input the third number"))



print(SiteSwapCheck(Num1,Num2,Num3))
