def show_board(board):
    '''
    This function will display and keep the tic tac toe board updated during the game.
    '''
    print(board[7]+'|'+board[8]+'|'+board[9])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[1]+'|'+board[2]+'|'+board[3])



def player_input():
    '''
    This function asks player 1 if they would like to Be X or O and assign the other to player 2.
    '''
    mark = ' '

    #Assign player 1

    while mark != 'X' and mark != 'O':
        mark = input('Player 1 would you like to be X or O? : ')
    player1 = mark

    #Assign player 2

    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'

    return (player1,player2)