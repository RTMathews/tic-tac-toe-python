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
    choice = ''
    accepted_list = [1,2,3,4,5,6,7,8,9]

    while choice not in accepted_list:
        choice = int(input('Enter the number of the cell you want to place your mark.: '))
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
        print('Player 1 goes first!')
    else:
        print('player 2 goes first!')

        
game_board = ['#','','','','','','','','','']