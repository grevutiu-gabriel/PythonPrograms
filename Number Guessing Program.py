import string
import random

Possible_Characters = string.digits


Target = input("Enter a number: ")
Attempt_This = ''.join(random.choice(Possible_Characters) for i in range(len(Target)))
Attempt_Next = ''

Completed = False

Attempt = 0

while Completed == False:
    print(Attempt_This)
    Attempt_Next = ''
    Completed = True
    for i in range(len(Target)):
        if Attempt_This[i] != Target[i]:
            Completed = False
            Attempt_Next += random.choice(Possible_Characters)
        else:
            Attempt_Next += Target[i]
    Attempt += 1
    Attempt_This = Attempt_Next

print("Tadaaaaaa!! That took " + str(Attempt) + " attempt(s)")
