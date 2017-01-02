# Import time module (if wanted)
import time
# Create loop
loop = True
# loop
while loop == True:
    # number (in order)
    for num in range(1,99999999999999999999999999999999999999999):

        # prime numbers are greater than 1
        if num > 1:
           # check for factors
           for i in range(2,num):
               if (num % i) == 0:
                   break
           else:
               print(num,"is a prime number")
               time.sleep(0.04)
       
        # if input number is less than
        # or equal to 1, it is not prime
