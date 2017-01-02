#treasure hunt
import random
#Virtual map
TheBeach=[[0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0]]

TheBeachGuesses=[[0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0]]

#Generating random position for treasure
row= random.randint(0,9)
collumn= random.randint(0,9)
TheBeach[(row)][(collumn)]=1

#Printing map
for x in TheBeachGuesses:
    print(x)
    
found = "0"
while "0" in found:
    guessx= int(input("What x co-ord do you want to try?")) -1
    guessy= 10- int(input("What y co-ord do you want to try?"))
    TheBeachGuesses[guessy][guessx]="X"
    
    if TheBeach[guessy][guessx]== 1:
        print("You win!")
        found="1"
        
    else:
        if guessx > (row -1):
            print("x was to high")
        if guessx < (row -1):
            print("x was to low")
        if guessx ==(row-1):
            print("You got the x")
            
        if guessy >(10 -collumn):
            print("y was to high")
        if guessy <(10 -collumn):
            print("y was to low")
        if guessy ==(10 - collumn):
            print("You got the y")
            
        print("Nope")
        
        #Printing map
        for x in TheBeachGuesses:
            print(x)
