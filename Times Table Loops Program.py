#times table

#loops conditional and count controlled

#starting my counter
nTimesTable = int(input("what is the times table you would like?"))
nUpTo= int(input("please tell me how high you'd like to go"))
for i in range (1,(nUpTo+1)):
    print (i,"x",nTimesTable,"=",i*nTimesTable)

if (i*nTimesTable) >9999:
    print ("avacado")

if 89>(i*nTimesTable) >87:
    print ("8.21 GigaWatts")
