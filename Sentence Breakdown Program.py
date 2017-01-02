#Sentence breakdown

#input Sentence to breakdown
Sentence= (input("What sentence would you like analysed?")).upper()

Alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
Location = []

#Breaking down sentence
for i in range (0,len(Sentence)):
    #Checking whether letter is in alphabet
    for x in range(0,len(Alphabet)):
        #checking letter
        if Alphabet[x] in Sentence[i]:
            #incrementing count and adding location
            Location.append((Alphabet[x],i))
        

print("They were located at positions",Location)
