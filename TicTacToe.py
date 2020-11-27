board_keys = []

GameBoard = {'7': ' ', '8': ' ', '9': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '1': ' ', '2': ' ', '3': ' '}

for key in GameBoard:
    board_keys.append(key)


def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

def game():
    player_piece = 'X'
    turn = 0

    for i in range(10):
        printBoard(GameBoard)
        print("It's your turn," + player_piece + ". Where would you like to move to?")

        move = input()

        if GameBoard[move] == ' ':
            GameBoard[move] = player_piece
            turn += 1
        else:
            print("That place is already filled.\nMove to which place?")
            continue

        if turn >= 5:
            if GameBoard['7'] == GameBoard['8'] == GameBoard['9'] != ' ':  
                printBoard(GameBoard)
                print("\nGame Over.\n")
                print(" **** " + player_piece + " won. ****")
                break
            elif GameBoard['4'] == GameBoard['5'] == GameBoard['6'] != ' ':  
                printBoard(GameBoard)
                print("\nGame Over.\n")
                print(" **** " + player_piece + " won. ****")
                break
            elif GameBoard['1'] == GameBoard['2'] == GameBoard['3'] != ' ':  
                printBoard(GameBoard)
                print("\nGame Over.\n")
                print(" **** " + player_piece + " won. ****")
                break
            elif GameBoard['1'] == GameBoard['4'] == GameBoard['7'] != ' ':  
                printBoard(GameBoard)
                print("\nGame Over.\n")
                print(" **** " + player_piece + " won. ****")
                break
            elif GameBoard['2'] == GameBoard['5'] == GameBoard['8'] != ' ':  
                printBoard(GameBoard)
                print("\nGame Over.\n")
                print(" **** " + player_piece + " won. ****")
                break
            elif GameBoard['3'] == GameBoard['6'] == GameBoard['9'] != ' ':  
                printBoard(GameBoard)
                print("\nGame Over.\n")
                print(" **** " + player_piece + " won. ****")
                break
            elif GameBoard['7'] == GameBoard['5'] == GameBoard['3'] != ' ':  
                printBoard(GameBoard)
                print("\nGame Over.\n")
                print(" **** " + player_piece + " won. ****")
                break
            elif GameBoard['1'] == GameBoard['5'] == GameBoard['9'] != ' ': 
                printBoard(GameBoard)
                print("\nGame Over.\n")
                print(" **** " + player_piece + " won. ****")
                break

        if turn == 9:
            print("\nGame Over.\n")
            print("It's a Tie!!")

        # Now we have to change the player after every move.
        if player_piece == 'X':
            player_piece = 'O'
        else:
            player_piece = 'X'

            # Now we will ask if player wants to restart the game or not.
    restart = input("Do want to play Again?(y/n)")
    if restart == "y" or restart == "Y":
        for key in board_keys:
            GameBoard[key] = " "

        game()


game()
