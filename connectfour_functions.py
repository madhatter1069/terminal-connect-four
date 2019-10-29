##Jared Clark 76551956 and Jack Callahan 37163374
import connectfour

def create_game():
    '''creates a new game and game board.'''
    this_game=connectfour.new_game()
    return this_game

def use_drop(gamestate: connectfour.GameState, col_num: int):
    '''takes the game move and uses the drop function'''
    gamestate=connectfour.drop(gamestate, col_num)
    return gamestate
    
def use_pop(gamestate: connectfour.GameState, col_num: int):
    '''takes the game move and uses the pop function'''
    game_state=connectfour.pop(gamestate, col_num)
    return game_state

def game_move(gamestate: connectfour.GameState):
    '''ask the user to type their game move'''
    game_move=input(_players_turn(gamestate))
    return game_move.upper()

def column_number(move: str):
    '''takes the game move and returns the column number and converts it to an int'''
    if move.startswith('DROP '):
        column_number=int(move[4:].strip())-1
        return column_number
    elif move.startswith('POP'):
        column_number=int(move[3:].strip())-1
        return column_number
          
def _printed_column_numbers():
    '''prints the number of each column above the play board'''
    col_num=0
    for col_num in range(connectfour.BOARD_COLUMNS):
        print(f' {col_num+1} ', end='')
    print()
    
def create_board():
    ''' prints a blank board at the start of every game'''
    _printed_column_numbers()
    for row in range(connectfour.BOARD_ROWS):#for each row in T
        for column in range(connectfour.BOARD_COLUMNS): # for each column in this row
            print(' • ', end="")
        print()
######################################VVVVVVVVVDONT TOUCH EVER!!!!!!!!!!!!!!!!!!!!!!!#############
def show_played_pieces(board:connectfour.GameState):
    '''prints the board part of the gamestate tuple in the correct print out'''
    _printed_column_numbers()
    for row in range(connectfour.BOARD_ROWS):
        for column in range(connectfour.BOARD_COLUMNS):
            if board.board[column][row]==1:
                print(' R ',end='')
            elif board.board[column][row]==2:
                print(' Y ',end='')
            else:
                print(' O ',end='')
        print()
######################################^^^^^^^^^^DONT TOUCH EVER!!!!!!!!!!!!!!!!!!!!!!!#############


def print_winner(game_state: connectfour.GameState):
    '''checks if there is a winner of the game yet and prints who it is if there is.'''
    if connectfour.winner(game_state)==0:
        return
            
    elif connectfour.winner(game_state)==1:
        print('WINNER: RED')
        return
                   
    elif connectfour.winner(game_state)==2:
        print('WINNER: YELLOW')
        return 

def _players_turn(game_state: connectfour.GameState):
    '''gives the color of who's turn it is.'''
    turn=''
    if game_state.turn==1:
        turn='RED: '
    elif game_state.turn==2:
        turn='YELLOW: '
    return turn

def end_game(game_state: connectfour.GameState):
    if connectfour.winner(game_state)!=0:
        return False
