##Jared Clark 76551956 and Jack Callahan 37163374
import connectfour_functions
import connectfour
def play_connect_four():
    print('Type DROP or POP and a space followed by the column number to place a piece.')
    connectfour_functions.create_board()
    this_game=connectfour_functions.create_game()
    while True:
        try:
            game_move=connectfour_functions.game_move(this_game)
            col_num=connectfour_functions.column_number(game_move)
            
            if col_num not in range(connectfour.BOARD_COLUMNS):
                print('That is not possible; try again.')
                
            elif game_move.startswith('DROP '):
                this_game=connectfour_functions.use_drop(this_game, connectfour_functions.column_number(game_move))
                connectfour_functions.show_played_pieces(this_game)
                connectfour_functions.print_winner(this_game)
                
            elif game_move.startswith('POP ') :
                this_game=connectfour_functions.use_pop(this_game, connectfour_functions.column_number(game_move))
                connectfour_functions.show_played_pieces(this_game)
                connectfour_functions.print_winner(this_game)

            else:
                print('That is not the correct command; try again.')

            if connectfour_functions.end_game(this_game) is False:
                return
        except:
            print('That is not possible; try again.')
            continue
    
if __name__ == '__main__':
    play_connect_four()
