#Siteswap checker array
#############################################################################
def SiteSwapCheck(Numbers):
    Numbers = Numbers.split()
    Allowed = True
    #Rule 1 (If divisible by 3)
    Total = 0
    for x in range(0, len(Numbers)):
        Total = Total + int(Numbers[x])
    if not ((Total)%3) == 0:
        Allowed = False


    #Rule 2 (no number after previous equal to one less than previous)
    for y in range(0, (len(Numbers)-1)):
        if int(Numbers[y]) == (int(Numbers[y+1]) + 1):  
            Allowed = False
            
    if int(Numbers[len(Numbers)-1]) == ((int(Numbers[0])) +1):
            Allowed = False

    if Allowed == False:
        return("INVALID SITESWAP")
############################################################################
Numbers = input("Please input your numbers")

print(SiteSwapCheck(Numbers))
