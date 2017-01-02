#Text game
Verbs= ["get", "put", "drop", "use", "enter", "leave", "walk", "search", "attack", "defend"]
Nouns= [["journal","bedroom"], ["magnifier","study"],["glasses","bathroom"], ["knife","kitchen"], ["kite","bedroom"], ["table","kitchen"], ["chair","kitchen"], ["key","hall"]]
rooms = ["hall","bedroom","study","kitchen","bathroom"]
room = "hall"
play= 0
while play == 0:
    Job= input("What would you like to do?")
    JobBreak= []
    
    for x in Job.split():
        JobBreak.append(x)

    print(JobBreak)

    if "get" in JobBreak[0]:
        for x in range(0, len(Nouns)):
            if JobBreak[1] in Nouns[x][0]:
                if room in Nouns[x][1]:
                    print("It's in your inventory")

        else:
            print("That's not here")

    if "go" in JobBreak[0]:
       for x in range(0, len(rooms)):
           if JobBreak[1] in rooms[x]:
              room = JobBreak[1]
              print("you are now in the", room)

    else:
        print("That's not a room")
                
        
    
    
