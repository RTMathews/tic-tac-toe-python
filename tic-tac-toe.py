import random

def show_board(board):
    '''
    This function will display and keep the tic tac toe board updated during the game.
    '''
    #prints tic-tac-toe board

    print(board[7]+'| '+board[8]+' |'+board[9])
    print(board[4]+'| '+board[5]+' |'+board[6])
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
        print(f'{mark} has won!')
        return True
    
    if board[4] == mark and board[5] == mark and board[6] == mark:
        print(f'{mark} has won!')
        return True
    
    if board[7] == mark and board[8] == mark and board[9] == mark:
        print(f'{mark} has won!')
        return True
    
    if board[1] == mark and board[5] == mark and board[9] == mark:
        print(f'{mark} has won!')
        return True
    
    if board[3] == mark and board[5] == mark and board[7] == mark:
        print(f'{mark} has won!')
        return True
    
    if board[1] == mark and board[4] == mark and board[7] == mark:
        print(f'{mark} has won!')
        return True
    
    if board[2] == mark and board[5] == mark and board[8] == mark:
        print(f'{mark} has won!')
        return True
    
    if board[3] == mark and board[6] == mark and board[9] == mark:
        print(f'{mark} has won!')
        return True
    

def choose_first():
    '''
    This function uses the randint function to decide which player goes first.
    '''

    first = random.randint(1,2)
    
    if first == 1:
        return 'Player 1 goes first!'
    else:
        return 'Player 2 goes first!'


def space_check(board,position):
    '''
    This function checks if a space is blank or if there is already a mark on it.
    '''
    if board[position] != '':
        return True
    else:
        return False
    

def full_board_check(board):
    '''
    This function checks if the board is full and there are no winners making it a draw.
    '''
    board_count = 0

    for spaces in board:
        if spaces != '':
            board_count += 1
        
        if board_count == 9:
            return True
        
        else:
            return False
        

def player_choice(board):
    '''
    This function asks the player for the cell number they would like to put their mark in.
    '''
    accepted_list = [1,2,3,4,5,6,7,8,9]

    position = ''

    while position not in accepted_list:
        position = int(input('Enter the number of the cell you want to place your mark.: '))

    while space_check(board,position) == True:
        position = int(input('This cell is already in use! Pick a different one.: '))

    return position


def replay():
    '''
    This function asks the player if they would like to play again.
    '''
    while again != 'Y' and again != 'N':
        again = input('Would you like to play again? (Y / N): ')
    
    if again == 'Y':
        return True
    else:
        return False
    
        
game_board = ['#','','','','','','','','','']