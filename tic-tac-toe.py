import random

def show_board(board):
    '''
    This function will display and keep the tic tac toe board updated during the game.
    '''
    #prints tic-tac-toe board

    print(board[7]+'|'+board[8]+'|'+board[9])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[1]+'|'+board[2]+'|'+board[3])


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

player_input()