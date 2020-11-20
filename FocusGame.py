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
        # initialize the coords, index 0
        for row in range(6):
            for col in range(6):
                self._full_board_list.append([(row, col)])
        # initialize the game pieces, index 1
        for x in range(0, len(self._full_board_list), 4):
            self._full_board_list[x].append("R")
        for x in range(1, len(self._full_board_list), 4):
            self._full_board_list[x].append("R")
        for x in range(2, len(self._full_board_list), 4):
            self._full_board_list[x].append("G")
        for x in range(3, len(self._full_board_list), 4):
            self._full_board_list[x].append("G")

    def get_full_board_list(self):
        return self._full_board_list

    def set_up_pieces(self):
        pieces = []
        for space in range(len(self._full_board_list)):
            pieces.append("r")
        return pieces

    def show_board(self):
        for row in range(0, 36, 6):
            print(self._full_board_list[row],
                  self._full_board_list[row+1],
                  self._full_board_list[row+2],
                  self._full_board_list[row+3],
                  self._full_board_list[row+4],
                  self._full_board_list[row+5],
                  )



def main():
    """for testing"""
    test_board = Board()
    print(test_board.get_full_board_list())
    # print(test_board.set_up_pieces())
    test_board.show_board()

    # READ ME
    # game = FocusGame(('PlayerA', 'R'), ('PlayerB', 'G'))
    # game.move_piece('PlayerA', (0, 0), (0, 1), 1)  # Returns message "successfully moved"
    # game.show_pieces((0, 1))  # Returns ['R','R']
    # game.show_captured('PlayerA')  # Returns 0
    # game.reserved_move('PlayerA', (0, 0))  # Returns message "No pieces in reserve"
    # game.show_reserve('PlayerA')  # Returns 0


if __name__ == '__main__':
    main()
