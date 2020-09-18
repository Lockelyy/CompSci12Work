import random

randnumber = random.randint(1,20)
print(randnumber)
print("The computer has chosen a number between 1 and 20\nDo your best to guess what it is!")

check = 0
while check == 0:
    userinput = input("Guess: ")
    userinput = int(userinput)
    
    if userinput == randnumber:
        print("You have guessed the number!")
        break

    if userinput > randnumber:
        print("You guessed too high! Try again")
    
    if userinput < randnumber:
        print("You guessed too low! Try again")
       
