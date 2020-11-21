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
# ---------------


class Board:
    """"""
    def __init__(self, p1_color, p2_color):  # could also call player objects
        """"""
        self._full_board_list = []
        # initialize the coords @ index 0
        for row in range(6):
            for col in range(6):
                self._full_board_list.append([(row, col)])
        # initialize the game pieces @ index 1 (base level)
        for x in range(0, len(self._full_board_list), 4):
            self._full_board_list[x].append(p1_color)
        for x in range(1, len(self._full_board_list), 4):
            self._full_board_list[x].append(p1_color)
        for x in range(2, len(self._full_board_list), 4):
            self._full_board_list[x].append(p2_color)
        for x in range(3, len(self._full_board_list), 4):
            self._full_board_list[x].append(p2_color)
        # # initialize the game pieces @ index 2 (2nd level)
        # for x in range(len(self._full_board_list)):
        #     self._full_board_list[x].append("*")
        # # initialize the game pieces @ index 3 (3rd level)
        # for x in range(len(self._full_board_list)):
        #     self._full_board_list[x].append("*")
        # # initialize the game pieces @ index 4 (4th level)
        # for x in range(len(self._full_board_list)):
        #     self._full_board_list[x].append("*")
        # # initialize the game pieces @ index 5 (5th level)
        # for x in range(len(self._full_board_list)):
        #     self._full_board_list[x].append("*")

    def get_full_board_list(self):
        """"""
        return self._full_board_list

    # def move_pieces(self, s_coord, e_coord, num_pieces):               # remove pieces from "top" and return the pieces picked up
    #     """"""
    #     picked_up = []                                      # hold pieces being moved
    #     for loc in self._full_board_list:
    #         if loc[0] == s_coord:                           # find start coord
    #             if num_pieces <= (len(loc)-1):              # check not trying to move more pieces than in stack
    #                 for i in range(num_pieces):             # for each piece being moved
    #                     picked_up += loc[len(loc)-1]        # add moved piece (from top of stack) to picked_up
    #                     del loc[len(loc)-1]                 # delete moved piece (from top of stack)
    #             else:
    #                 return "invalid number of pieces"       # msg if trying to move more pieces than in stack
    #     for loc in self._full_board_list:
    #         if loc[0] == e_coord:                           # find coord
    #             for i in range(len(picked_up), 0, -1):         # for each piece in pieces, backwards from the end
    #                 loc.append(picked_up[i-1])                 # add piece (one by one) to coord
    #     return "successfully moved"

    def remove_pieces(self, coord, num_pieces):             # remove pieces from "top" and return the pieces picked up
        """"""
        for loc in self._full_board_list:
            if loc[0] == coord:                             # find coord
                picked_up = []                              # hold pieces being moved
                if num_pieces <= (len(loc)-1):              # check not trying to move more pieces than in stack
                    for i in range(num_pieces):             # for each piece being moved
                        picked_up += loc[len(loc)-1]        # add moved piece (from top of stack) to picked_up
                        del loc[len(loc)-1]                 # delete moved piece (from top of stack)
                    return picked_up                        # return stack of moved pieces
                else:
                    return "invalid number of pieces"       # msg if trying to move more pieces than in stack

    def place_pieces(self, coord, pieces):                  # place list of pieces
        """"""
        for loc in self._full_board_list:
            if loc[0] == coord:                             # find coord
                for i in range(len(pieces), 0, -1):         # for each piece in pieces, backwards from the end
                    loc.append(pieces[i-1])                 # add piece (one by one) to coord

    def show_board(self):
        for row in range(0, 36, 6):
            # print(self._full_board_list[row][1],
            #       self._full_board_list[row+1][1],
            #       self._full_board_list[row+2][1],
            #       self._full_board_list[row+3][1],
            #       self._full_board_list[row+4][1],
            #       self._full_board_list[row+5][1],
            #       )
            # print(f"{self._full_board_list[row][1]}{self._full_board_list[row][2]}{self._full_board_list[row][3]}"
            #       f"{self._full_board_list[row][4]}{self._full_board_list[row][5]}",
            #       f"{self._full_board_list[row+1][1]}{self._full_board_list[row+1][2]}{self._full_board_list[row+1][3]}"
            #       f"{self._full_board_list[row+1][4]}{self._full_board_list[row+1][5]}",
            #       f"{self._full_board_list[row+2][1]}{self._full_board_list[row+2][2]}{self._full_board_list[row+2][3]}"
            #       f"{self._full_board_list[row+2][4]}{self._full_board_list[row+2][5]}",
            #       f"{self._full_board_list[row+3][1]}{self._full_board_list[row+3][2]}{self._full_board_list[row+3][3]}"
            #       f"{self._full_board_list[row+3][4]}{self._full_board_list[row+3][5]}",
            #       f"{self._full_board_list[row+4][1]}{self._full_board_list[row+4][2]}{self._full_board_list[row+4][3]}"
            #       f"{self._full_board_list[row+4][4]}{self._full_board_list[row+4][5]}",
            #       f"{self._full_board_list[row+5][1]}{self._full_board_list[row+5][2]}{self._full_board_list[row+5][3]}"
            #       f"{self._full_board_list[row+5][4]}{self._full_board_list[row+5][5]}"
            #       )
        # if len(self._full_board_list[row+1]) > 2:
        #     for x in range(1, len(self._full_board_list[row+1])):
        #         print(self._full_board_list[row+1][x])
        # else:
        #     print("*")
            for col in range(6):
                list_len = (len(self._full_board_list[row+col]))
                for num in range(1, list_len):
                    print(self._full_board_list[row+col][num], end="")
                print((5 - (len(self._full_board_list[row+col])-1)) * "*", end=" ")
            print("")
        print("-----------------------------------")


# class Player
#   init method
#       _captured_pieces = 0
#       _reserve_pieces = 0
#   get_reserve_pieces:
#       return
#   set_reserve_pieces:
#       change reserve pieces
class Player:
    """"""
    def __init__(self, name, color):
        """"""
        self._player_name = name
        self._player_color = color
        self._captured_pieces = 0
        self._reserve_pieces = 0

    def get_player_name(self):
        return self._player_name

    def get_player_color(self):
        return self._player_color

    def get_captured_pieces(self):
        return self._captured_pieces

    def get_reserve_pieces(self):
        return self._reserve_pieces


# class FocusGame
#   init method, (("player1_name", "p1_color"), ("player2_name", "p2_color")):
#       board being a list of lists, don't include 1x4 side extensions
#       initialize the pieces on the board, from (0,0) to (5,5), (row, col)
#       _turn = None
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
class FocusGame:
    """"""
    def __init__(self, p1_tup, p2_tup):
        """"""
        self._player1 = Player(p1_tup[0], p1_tup[1])
        self._player2 = Player(p2_tup[0], p2_tup[1])
        self._board = Board(self._player1.get_player_color(), self._player2.get_player_color())
        self._turn = None

    def move_piece(self, move_p_name, start_loc, end_loc, num_pieces):
        """"""
        p_turn = None
        if move_p_name == self._player1.get_player_name():
            p_turn = self._player1
        elif move_p_name == self._player2.get_player_name():
            p_turn = self._player2
        else:
            return "who's trying to butt in"

        if self._turn is None:          # on first move, set player turn
            self._turn = move_p_name

        if move_p_name != self._turn:   # check if it's player's turn
            return "not your turn"

        # invalid locations (source or destination): return "invalid location"
        if not -1 < start_loc[0] < 6 or not -1 < start_loc[1] < 6 or not -1 < end_loc[0] < 6 or not -1 < end_loc[1] < 6:
            return "invalid location"

        picked_up = []  # hold pieces being moved
        for loc in self._board.get_full_board_list():
            if loc[0] == start_loc:  # find start coord
                if loc[len(loc) - 1] != p_turn.get_player_color():  # check if piece on top is player's whose turn it is
                    return "not your stack to move"
                elif num_pieces <= (len(loc) - 1):  # check not trying to move more pieces than in stack
                    for i in range(num_pieces):  # for each piece being moved
                        picked_up += loc[len(loc) - 1]  # add moved piece (from top of stack) to picked_up
                        del loc[len(loc) - 1]  # delete moved piece (from top of stack)
                else:
                    return "invalid number of pieces"  # msg if trying to move more pieces than in stack
        for loc in self._board.get_full_board_list():
            if loc[0] == end_loc:  # find coord
                for i in range(len(picked_up), 0, -1):  # for each piece in pieces, backwards from the end
                    loc.append(picked_up[i - 1])  # add piece (one by one) to coord
        if move_p_name == self._player1.get_player_name():  # alternate turns
            self._turn = self._player2.get_player_name()
        else:
            self._turn = self._player1.get_player_name()
        return "successfully moved"

#       check if stack is > 5:
#           capture bottom pieces that belong to other player
#           reserve bottom pieces that belong to current player
#       check if player wins, either player has captured pieces >= 6
#           return "<player_name> Wins"


def main():
    """for testing"""
    # test Board class
    # test_board = Board()
    # print(test_board.get_full_board_list())
    # test_board.show_board()
    # for x in test_board.get_full_board_list():
    #     if x[0] == (5, 3):
    #         print(x[1])
    # test_board.remove_piece((0, 1))
    # # test_board.show_board()
    # test_board.place_piece((0, 1), "N")
    # test_board.place_piece((0, 1), "N")
    # # print(test_board.get_full_board_list())
    # # test_board.show_board()
    # test_board.place_piece((0, 1), "R")
    # test_board.place_piece((0, 1), "G")
    # # test_board.remove_piece((0, 1))
    # # test_board.remove_piece((0, 1))
    # test_board.place_piece((1, 1), "N")
    # test_board.place_piece((1, 1), "N")
    # test_board.remove_piece((0, 0))
    # test_board.remove_piece((0, 1))
    # test_board.remove_piece((0, 2))
    # test_board.remove_piece((0, 3))
    # test_board.remove_piece((0, 4))
    # test_board.remove_piece((0, 5))
    # test_board.remove_piece((3, 0))
    # test_board.remove_piece((3, 1))
    # test_board.remove_piece((3, 2))
    # test_board.remove_piece((3, 3))
    # test_board.remove_piece((3, 4))
    # test_board.remove_piece((3, 5))
    # test_board.place_piece((0, 0), "R")
    # test_board.place_piece((1, 0), "R")
    # test_board.place_piece((2, 0), "R")
    # test_board.place_piece((3, 0), "R")
    # test_board.place_piece((4, 0), "R")
    # test_board.place_piece((5, 0), "R")
    # print(test_board.get_full_board_list())
    # test_board.show_board()
    # test_board = Board("R", "G")
    # test_board.place_pieces((0, 1), ["L", "M", "N", "O"])
    # print(test_board.get_full_board_list())
    # test_board.show_board()
    # stack = test_board.remove_pieces((0, 1), 3)
    # print(stack)
    # test_board.place_pieces((0, 0), stack)
    # print(test_board.get_full_board_list())
    # test_board.move_pieces((0, 0), (0, 1), 1)
    # test_board.move_pieces((0, 1), (0, 2), 2)
    # test_board.show_board()

    game = FocusGame(('PlayerA', 'R'), ('PlayerB', 'G'))
    # # print(game._player1.get_player_color())
    # # print(game._player2.get_player_name())
    # # print(game._player2.get_captured_pieces())
    print(game.move_piece("PlayerA", (0, 0), (0, 1), 1))
    print(game.move_piece("PlayerB", (0, 2), (0, 3), 1))
    print(game.move_piece("PlayerA", (0, 1), (0, 4), 2))
    print(game.move_piece("PlayerB", (0, 3), (0, 5), 2))
    print(game.move_piece("PlayerA", (0, 4), (0, 1), 3))
    print(game.move_piece("PlayerB", (0, 5), (0, 2), 3))
    print(game.move_piece("PlayerA", (0, 1), (0, 1), 1))
    # print(game.move_piece("PlayerB", (0, 1), (0, 2), 1))
    game._board.show_board()

    # READ ME
    # game = FocusGame(('PlayerA', 'R'), ('PlayerB', 'G'))
    # game.move_piece('PlayerA', (0, 0), (0, 1), 1)  # Returns message "successfully moved"
    # game.show_pieces((0, 1))  # Returns ['R','R']
    # game.show_captured('PlayerA')  # Returns 0
    # game.reserved_move('PlayerA', (0, 0))  # Returns message "No pieces in reserve"
    # game.show_reserve('PlayerA')  # Returns 0


if __name__ == '__main__':
    main()
