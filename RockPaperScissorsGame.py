import random


options = ["Rock", "Paper", "Scissors"]
computer_input = options[random.randint(0, 2)]

#set player to False
checker = False

while checker == False:

    player_input = input("\nRock, Paper or Scissors?: ")

    if player_input == computer_input:
        print("\nIts a tie!")

    elif player_input == "Rock":
        if computer_input == "Paper":
            print("\nYou lose", computer_input + " smothers " + player_input)
        else:
            print("\nYou win!", player_input + " wrecks " + computer_input)

    elif player_input == "Paper":
        if computer_input == "Scissors":
            print("\nYou lose", computer_input + " cuts " + player_input)
        else:
            print("\nYou win!" + player_input + " smothers " + computer_input)

    elif player_input == "Scissors":
        if computer_input == "Rock":
            print("\nYou lose" + computer_input + " wrecks " + player_input)
        else:
            print("You win!" + player_input + " cuts " + computer_input)

    else:
        print("Invalid input, please check capitlatization!!")

    player_input = False
    computer_input = options[random.randint(0, 2)]
