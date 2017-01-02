studentName= str(input("What is your name?"))
studentMark= int(input("What mark did you get?"))
totalMark= int(input("What were the total marks available?"))

percentage= int((100/totalMark)*studentMark)

if (percentage>80):
    print("Congratulations", studentName ,"you got", percentage,"%")
elif (percentage>60) or (percentage== 60):
    print("Could have done better", studentName ,"you only got", percentage,"%")
elif (percentage<60):
    print("Really?", studentName ,"you really got", percentage,"%?")

import urllib


open("Matrix")



