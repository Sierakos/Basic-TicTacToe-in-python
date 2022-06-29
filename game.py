import random

def ticTacToeGame():
    menu()

def game():
    print("  1  |  2  |  3  ")
    print("-----------------")
    print("  4  |  5  |  6  ")
    print("-----------------")
    print("  7  |  8  |  9  ")

    ### board for our game ###
    board = [" ", " ", " ",
             " ", " ", " ",
             " ", " ", " "]
    while True: 

    ### first player turn next bot ###
        playerTurn(board)
        checkResult(board)
        botTurn(board)
        checkResult(board)

    ### every time player and bot make a move redraw board ###
        drawBoard(board)
        
def playerTurn(board):
    while True:
        player_choice = int(input("Your turn. Choose your place."))
        if ckeckIfLegalMove(player_choice, board) == True:
            board[player_choice - 1] = "X"
            break
        else:
            print("This spot is occupied. Choose another spot.")

def botTurn(board):
    while True:
        bot_choice = random.randint(1, 9)
        if ckeckIfLegalMove(bot_choice, board) == True:
            board[bot_choice - 1] = "O"
            break
    
def ckeckIfLegalMove(player_choice, board):
    if board[player_choice - 1] != " ":
        return False
    else:
        return True
    
def menu():
    choice = 0
    while True:
        print("-"*50)
        print("WELCOME TO TIC-TAC-TOE")
        print("1. Start")
        print("2. Exit")
        choice = int(input("Choose your option and click Enter: "))
        if choice == 1:
            game()
        elif choice == 2:
            exit()

def drawBoard(board):
    print("  " + board[0] + "  |  " + board[1] + "  |  " + board[2] + "  ")
    print("-----------------")
    print("  " + board[3] + "  |  " + board[4] + "  |  " + board[5] + "  ")
    print("-----------------")
    print("  " + board[6] + "  |  " + board[7] + "  |  " + board[8] + "  ")

def checkResult(board):
    win_combinations = [[0,1,2], [3,4,5], [6,7,8], [0,4,8], [2,4,6], [0,3,6], [1,4,7], [2,5,8]]

    for i in win_combinations:
        ### Player wins ###
        if (board[i[0]] == "X" and board[i[1]] == "X" and board[i[2]] == "X"):
            print("You won CONGRATULATIONS!!!")
            menu()

        ### Bot wins ###
        elif (board[i[0]] == "O" and board[i[1]] == "O" and board[i[2]] == "O"):
            drawBoard(board)
            print("You lost try again")
            menu()     

    ### Draw ###
    if not " " in board:
        print("Draw!")
        menu()
    