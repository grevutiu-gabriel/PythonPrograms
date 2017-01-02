
print("Please use a ? for the unknown value")
Speed=input("What is the speed?")
time=input("What is the time?")
Distance=input("What is the distance?")
if (Speed=='?' and Distance=='?') or (Speed=='?' and time =='?') or (time=='?' and Distance=='?'):
    print("There are too many variables")
elif Speed =='?':
    Speed= int(Distance)/int(time)
    print("The speed is", Speed)
elif time =='?':
    time= int(Distance)/int(Speed)
    print("The timne is",time)
elif Distance =='?':
    Distance= int(Speed)*int(time)
    print("The Distance is",Distance)
else:
    print("You have all the answers")
