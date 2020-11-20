# Name: Wes MacDonald
# Date: 11/20/2020
# Description:

# Pseudocode
# class FocusGame
#   init method, (("player1_name", "p1_color"), ("player2_name", "p2_color")):
#       board being a list of lists, don't include 1x4 side extensions
#       initialize the pieces on the board, from (0,0) to (5,5), (row, col)
#   move_piece method ("player_name", (start_loc coord), (end_loc coord), num_pieces)
#       check if move is valid
#           player move out of turn: return "not your turn"
#           invalid locations (source or destination): return "invalid location"
#           player move invalid num of pieces: return "invalid number of pieces"
#       make move, edit lists...
#       return "successfully moved
#       check if stack is > 5:
#           capture bottom pieces that belong to other player
#           reserve bottom pieces that belong to current player
#       check if player wins, either player has captured pieces >= 6
#           return "<player_name> Wins"
#   show_pieces method, (loc coord)
#       return list of pieces at that location, [bottom piece, ..., top piece]
#   show_reserve method, ("player_name")
#       return player_name.get_reserve_pieces
#   show_captured method, ("player_name")
#       return player_name.get_captured_pieces
#   reserved_move method ("player_name", loc coord)
#       if player_name.get_reserve_pieces >= 1
#           player_name.set_reserve_pieces(player_name.get_reserve_pieces - 1)
#           play piece to loc coord
#       else
#           return "no pieces in reserve"
# class Player
#   init method
#       _captured_pieces = 0
#       _reserve_pieces = 0
#   get_reserve_pieces:
#       return
#   set_reserve_pieces:
#       change reserve pieces
# class Board
#   init method
#       set up board
#       full_board_list = []
#       for row in range(5):
#           for col in range(5):
#               full_board_list.append [row, col]

class Board:
    """"""
    def __init__(self):
        self._full_board_list = []
        for row in range(6):
            for col in range(6):
                self._full_board_list.append([row, col])

    def get_full_board_list(self):
        return self._full_board_list


def main():
    """for testing"""
    test_board = Board()
    print(test_board.get_full_board_list())

    # READ ME
    # game = FocusGame(('PlayerA', 'R'), ('PlayerB', 'G'))
    # game.move_piece('PlayerA', (0, 0), (0, 1), 1)  # Returns message "successfully moved"
    # game.show_pieces((0, 1))  # Returns ['R','R']
    # game.show_captured('PlayerA')  # Returns 0
    # game.reserved_move('PlayerA', (0, 0))  # Returns message "No pieces in reserve"
    # game.show_reserve('PlayerA')  # Returns 0


if __name__ == '__main__':
    main()
