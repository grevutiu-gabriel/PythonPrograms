#Calculator
Calculation= input("What calculation would you like?")
CalcBreakdown= []
for x in Calculation.split():
    CalcBreakdown.append(x)
    
print(CalcBreakdown)
Brian = 1
finalNumber= CalcBreakdown[0]

for y in range(1,len(CalcBreakdown)):
    if "+" in CalcBreakdown[1]:
        finalNumber=int(finalNumber) + int(Brian + 1)
        print(finalNumber)
        
    if "*" in CalcBreakdown[1]:
        finalNumber=int(finalNumber) * int(Brian + 1)
        print(finalNumber)

    if "/" in CalcBreakdown[Brian]:
        finalNumber=int(finalNumber) / int(Brian + 1)
        print(finalNumber)

    if "-" in CalcBreakdown[1]:
        finalNumber=int(finalNumber) - int(Brian + 1)
        print(finalNumber)

    Brian= Brian +2
