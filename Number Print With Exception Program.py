#Number print with exception
def Number():
    Success = 0

    while Success == 0:
        Number = input("What number would you like?")
        try:
            Number= int(Number)
            print(Number)
            Success = 1

        except ValueError as error:
            print("That is not a number, try again (", error, ")")

Number()
