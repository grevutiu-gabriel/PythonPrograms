# Importing Modules
import random

# Creating Variables/Arrays
Pack_Of_Cards = []
Suites = ["Hearts", "Clubs", "Spades", "Diamonds"]
Value = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
# Setting Values/Creating Variables
Suites_Number = 0
Value_Number = 0
# While statement loop to continue card making until all suites are done
while Suites_Number <= 3:
    # Combining cards together and adding them to the Pack of Cards Array
    # Cards combined and chosen by changing numbers
    Pack_Of_Cards.append((Value[Value_Number]) + " of " + (Suites[Suites_Number]))
    # Increasing the number of cards currently done
    Value_Number = (Value_Number + 1)
    # When the cards number reaches 13 it resets it and increases the suit number by one
    # As a full suit has now been created
    if Value_Number == 13:
        Suites_Number = (Suites_Number + 1)
        # Resetting Card number for next suit
        Value_Number = 0

# Printing Cards/Array with no '' in them
print(' '.join(Pack_Of_Cards))

Value_Position = random.randint(0,12)
Chosen_First_Card_Value = (Value_Position + 1)
First_Card = Pack_Of_Cards[Value_Position]

print("First Card:",First_Card)

Value_Position = random.randint(0,12)
Chosen_Second_Card_Value = (Value_Position + 1)
Second_Card = Pack_Of_Cards[Value_Position]

print("First Card:",Second_Card)

if Chosen_First_Card_Value > Chosen_Second_Card_Value:
    print("First card wins")

else:
    print("Second card wins")
