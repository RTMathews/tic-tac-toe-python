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


def player_position(board, mark, position):
    '''
    This function will ask the player which tile they want to place their mark in, 1 - 9.
    '''
    accepted_values = [1,2,3,4,5,6,7,8,9]

    while position not in accepted_values and position != '':
        position = input("Choose your next position: (1-9)")
        if position == '':
            board[position].replace('',mark)

    return board

def check_win(board):
    '''
    This function checks the board to see if there is a winner or a draw.
    '''
    is_won = False
    is_draw = False
    tiles_used = 0

    #A lot of if statements checking if X won

    if board[1] == 'X' and board[2] == 'X' and board[3] == 'X':
        is_won = True
        print('X Wins!')
        return is_won
    
    if board[4] == 'X' and board[5] == 'X' and board[6] == 'X':
        is_won = True
        print('X Wins!')
        return is_won
    
    if board[7] == 'X' and board[8] == 'X' and board[9] == 'X':
        is_won = True
        print('X Wins!')
        return is_won
    
    
    if board[1] == 'X' and board[5] == 'X' and board[9] == 'X':
        is_won = True
        print('X Wins!')
        return is_won
    
    if board[3] == 'X' and board[5] == 'X' and board[7] == 'X':
        is_won = True
        print('X Wins!')
        return is_won
    
    #A lot of if statements checking if O won

    if board[1] == 'O' and board[2] == 'O' and board[3] == 'O':
        is_won = True
        print('O Wins!')
        return is_won
    
    if board[4] == 'O' and board[5] == 'O' and board[6] == 'O':
        is_won = True
        print('O Wins!')
        return is_won
    
    if board[7] == 'O' and board[8] == 'O' and board[9] == 'O':
        is_won = True
        print('O Wins!')
        return is_won
    
    if board[1] == 'O' and board[5] == 'O' and board[9] == 'O':
        is_won = True
        print('O Wins!')
        return is_won
    
    if board[3] == 'O' and board[5] == 'O' and board[7] == 'O':
        is_won = True
        print('O Wins!')
        return is_won
    
    #Checks if all of the tiles are full and no one won
    
    for tile in board:
        if tile != '':
            tiles_used += 1
            if tiles_used == 9:
                is_draw = True
                print("It's a Draw!")
                return is_draw