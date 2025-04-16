import random

def show_board(board):
    '''
    This function will display and keep the tic tac toe board updated during the game.
    '''
    #prints tic-tac-toe board

    print(board[7]+'| '+board[8]+' |'+board[9])
    print('-------')
    print(board[4]+'| '+board[5]+' |'+board[6])
    print('-------')
    print(board[1]+'| '+board[2]+' |'+board[3])


def player_input():
    '''
    This function let's player 1 decide if they want to have X or O as their mark.
    '''
    mark = ''

    while mark != 'X' and mark != 'O':
        mark = input('Player 1 would you like to play as X or O?: ')
        if mark == 'X':
            player1_mark = 'X'
            player2_mark = 'O'
        else:
            player1_mark = 'O'
            player2_mark = 'X'
    
    return (player1_mark, player2_mark)


def place_mark(board,mark,position):
    '''
    This function let's the player choose which cell to put their mark in.
    '''
    board[position] = mark


def win_check(board,mark):
    '''
    This function checks to see if the current player has won.
    '''
    if board[1] == mark and board[2] == mark and board[3] == mark:
        return True
    
    if board[4] == mark and board[5] == mark and board[6] == mark:
        return True
    
    if board[7] == mark and board[8] == mark and board[9] == mark:
        return True
    
    if board[1] == mark and board[5] == mark and board[9] == mark:
        return True
    
    if board[3] == mark and board[5] == mark and board[7] == mark:
        return True
    
    if board[1] == mark and board[4] == mark and board[7] == mark:
        return True
    
    if board[2] == mark and board[5] == mark and board[8] == mark:
        return True
    
    if board[3] == mark and board[6] == mark and board[9] == mark:
        return True
    

def choose_first():
    '''
    This function uses the randint function to decide which player goes first.
    '''

    first = random.randint(1,2)
    
    if first == 1:
        return 'Player 1'
    else:
        return 'Player 2'


def space_check(board,position):
    '''
    This function checks if a space is blank or if there is already a mark on it.
    '''
    if board[position] != ' ':
        return True
    else:
        return False
    

def full_board_check(board):
    '''
    This function checks if the board is full and there are no winners making it a draw.
    '''
    space = 0

    while True:
        for spaces in board:
            if spaces != ' ':
                space += 1
                if space == 10:
                    return True
        else:
            break

        

def player_choice(board):
    '''
    This function asks the player for the cell number they would like to put their mark in.
    '''
    accepted_list = [1,2,3,4,5,6,7,8,9]

    position = ' '

    while position not in accepted_list or space_check(board,position):
        position = int(input('Enter the number of the cell you want to place your mark.: '))

    return (position)


def replay():
    '''
    This function asks the player if they would like to play again.
    '''
    again = ' '
    
    while again != 'Y' and again != 'N':
        again = input('Would you like to play again? (Y / N): ')
    
    if again == 'Y':
        return True
    else:
        return False


#Game setup
while True:
    print('Welcome to Tic-Tac-Toe!')

    game_board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']

    play_game = input('Are you ready to play? (Y / N): ')
    if play_game == 'Y':
        game_on = True
    else:
        game_on = False

    player1_mark,player2_mark = player_input()

    turn = choose_first()
    print(turn + ' goes first!')

    show_board(game_board)

    #while game_on, play
    while game_on:
        if turn == 'Player 1':
            #Player 1 Turn
            print('Player 1, ')
            position = player_choice(game_board)

            place_mark(game_board,player1_mark,position)

            print(show_board(game_board))

            if win_check(game_board,player1_mark):
                print("Player 1 Wins!")
                game_on = False
            else:
                if full_board_check(game_board):
                    print("It's a Tie!")
                    game_on = False
                    break
                else:
                    turn = 'Player 2'


        #Player 2 Turn
        print('Player 2, ')
        if turn == 'Player 2':
            position = player_choice(game_board)

            place_mark(game_board,player2_mark,position)

            print(show_board(game_board))

            if win_check(game_board,player2_mark):
                print("Player 2 Wins!")
                game_on = False
            else:
                if full_board_check(game_board):
                    print("It's a Tie!")
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break