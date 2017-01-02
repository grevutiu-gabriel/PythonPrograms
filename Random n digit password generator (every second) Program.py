#Random n digit password generator, every second
import time
import random


list1 =['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9']

Length= 100
Password= []
loop = 1
while loop == 1:
    for y in range (0,Length):
        Password.append(random.choice(list1))
        
    print('7'.join(Password))
	time.sleep(1)

    Password= []

