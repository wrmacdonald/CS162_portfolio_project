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
    """represents a board"""
    def __init__(self, p1_color, p2_color):
        """initializes a board object
        :param p1_color: player 1 piece color
        :type p1_color: str
        :param p2_color: player 2 piece color
        :type p2_color: str
        """
        # list to hold lists of coords for each space on the board @ index 0, and piece(s) in a stack at that coord
        # pieces start @ index 1 (bottom/base of stack), to the end of the list (top of stack)
        self._full_board_list = []

        # initialize tuples of the coords @ index 0 of the list
        for row in range(6):
            for col in range(6):
                self._full_board_list.append([(row, col)])

        # initialize the game pieces @ index 1 (bottom level) for game set-up
        for x in range(0, len(self._full_board_list), 4):
            self._full_board_list[x].append(p1_color)
        for x in range(1, len(self._full_board_list), 4):
            self._full_board_list[x].append(p1_color)
        for x in range(2, len(self._full_board_list), 4):
            self._full_board_list[x].append(p2_color)
        for x in range(3, len(self._full_board_list), 4):
            self._full_board_list[x].append(p2_color)

    def get_full_board_list(self):
        """get method for _full_board_list
        :return: a list of lists of the board, containing coords and pieces @ each coord
        :rtype: list
        """
        return self._full_board_list

    def show_board(self):
        """method to show the board in a visually understandable way, * = empty space"""
        for row in range(0, 36, 6):
            for col in range(6):
                list_len = (len(self._full_board_list[row+col]))
                for num in range(1, list_len):
                    print(self._full_board_list[row+col][num], end="")
                print((5 - (len(self._full_board_list[row+col])-1)) * "*", end=" ")
            print("")
        print("-----------------------------------")


class Player:
    """represents a player"""
    def __init__(self, name, color):
        """initializes a player object
        :param name: name of player
        :type name: str
        :param color: color of player pieces
        :type color: str
        """
        self._player_name = name
        self._player_color = color
        self._captured_pieces = 0
        self._reserve_pieces = 0

    def get_player_name(self):
        """get method for _player_name
        :return: player's name
        :rtype: str
        """
        return self._player_name

    def get_player_color(self):
        """get method for _player_color
        :return: player's color
        :rtype: str
        """
        return self._player_color

    def get_captured_pieces(self):
        """get method for player's _captured_pieces
        :return: player's _captured_pieces
        :rtype: int
        """
        return self._captured_pieces

    def set_captured_pieces(self, num_piece):
        """set method for player's _captured_pieces, +1 to add a piece, -1 to remove a piece
        :param num_piece: piece(s) to add to or remove from a player's captured pieces
        :type num_piece: int
        """
        self._captured_pieces += num_piece

    def get_reserve_pieces(self):
        """get method for player's _reserve_pieces
        :return: player's _reserve_pieces
        :rtype: int
        """
        return self._reserve_pieces

    def set_reserve_pieces(self, num_piece):
        """set method for player's _reserve_pieces, +1 to add a piece, -1 to remove a piece
        :param num_piece: piece(s) to add to or remove from a player's reserve pieces
        :type num_piece: int
        """
        self._reserve_pieces += num_piece


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
    """represents the game"""
    def __init__(self, p1_tup, p2_tup):
        """initializes a game object
        :param p1_tup: strings of player1_name and player1_color
        :type p1_tup: tuple
        :param p2_tup: strings of player2_name and player2_color
        :type p2_tup: tuple
        """
        self._player1 = Player(p1_tup[0], p1_tup[1])
        self._player2 = Player(p2_tup[0], p2_tup[1])
        self._board = Board(self._player1.get_player_color(), self._player2.get_player_color())
        self._turn = self._player1

    def validate_move(self, player_name, start_loc, end_loc, num_pieces):
        """checks the validity of any moves
        :param player_name: name of player who's trying to move
        :type player_name: str
        :param start_loc: coord to move pieces from
        :type start_loc: tuple
        :param end_loc: coord to move pieces to
        :type end_loc: tuple
        :param num_pieces: number of pieces to move
        :type num_pieces: int
        :return: notification codes for whether the move is valid or not
        :rtype: str
        """
        if player_name != self._turn.get_player_name():   # check if it's player's turn
            return "n_y_t"  # Not_Your_Turn code

        # check locations are possible spaces on board
        if not -1 < start_loc[0] < 6 or not -1 < start_loc[1] < 6:
            return "i_s_l"  # Illegal_Start_Location code
        if not -1 < end_loc[0] < 6 or not -1 < end_loc[1] < 6:
            return "i_e_l"  # Illegal_End_Location code

        # check if end_loc is num_pieces away from start_loc, and only vertical or horizontal move
        row_move = abs(start_loc[0] - end_loc[0])
        column_move = abs(start_loc[1] - end_loc[1])
        if not ((row_move == 0 and column_move == num_pieces) or (row_move == num_pieces and column_move == 0)):
            return "i_l"  # Illegal_Location code

        # check stack for: if piece on top belongs to turn player, & player not trying to move more pieces than in stack
        for loc in self._board.get_full_board_list():  # loop through locations on board
            if loc[0] == start_loc:  # find start coord
                if loc[-1] != self._turn.get_player_color():  # check if piece on top belongs to turn player
                    return "i_l"
                elif num_pieces > (len(loc) - 1):  # check not trying to move more pieces than in stack
                    return "i_n_o_p"  # Invalid_Number_Of_Pieces code

    def move_piece(self, player_name, start_loc, end_loc, num_pieces):
        """move method, for single and multiple moves
        :param player_name: name of player who's trying to move
        :type player_name: str
        :param start_loc: coord to move pieces from
        :type start_loc: tuple
        :param end_loc: coord to move pieces to
        :type end_loc: tuple
        :param num_pieces: number of pieces to move
        :type num_pieces: int
        :return: notification messages, or False for whether the move was completed successfully or not
        :rtype: str or bool
        """
        # check if move is valid
        val = self.validate_move(player_name, start_loc, end_loc, num_pieces)
        if val == "n_y_t":
            return False
        elif val == "i_l" or val == "i_s_l" or val == "i_e_l":
            return False
        elif val == "i_n_o_p":
            return False

        # move
        picked_up = []  # hold pieces being moved
        for loc in self._board.get_full_board_list():  # loop through locations on board
            if loc[0] == start_loc:  # find start coord
                for i in range(num_pieces):  # for each piece being moved
                    picked_up += loc[len(loc) - 1]  # add moved piece (from top of stack) to picked_up
                    del loc[len(loc) - 1]  # delete moved piece (from top of stack)
        for loc in self._board.get_full_board_list():  # loop through locations on board
            if loc[0] == end_loc:  # find end coord
                for i in range(len(picked_up), 0, -1):  # for each piece in pieces, backwards from the end
                    loc.append(picked_up[i - 1])  # add piece (one by one) to coord

        # check if stack is > 5
        player_obj = self.get_player_object(player_name)
        self.check_height(player_obj, end_loc)

        # check win condition
        if player_obj.get_captured_pieces() >= 6:
            return f"{player_obj.get_player_name()} Wins"

        # alternate turn
        self.set_turn(player_name)

        return "successfully moved"

    def reserved_move(self, player_name, location):
        """move method for moving a piece from player's own reserve
        :param player_name: name of player who's trying to move
        :type player_name: str
        :param location: coord to move piece to
        :type location: tuple
        :return: notification messages, or False for whether the move was completed successfully or not
        :rtype: str or bool
        """
        # check if move is valid
        val = self.validate_move(player_name, (0, 0), location, 1)
        if val == "n_y_t":
            return False
        elif val == "i_e_l":
            return False

        # move
        player_obj = self.get_player_object(player_name)  # check there's pieces in player's reserve
        if player_obj.get_reserve_pieces() <= 0:
            return False
        else:  # add piece to board location
            for loc in self._board.get_full_board_list():  # loop through locations on board
                if loc[0] == location:
                    loc.append(player_obj.get_player_color())  # add player's piece to location on board
        player_obj.set_reserve_pieces(-1)  # remove piece from player's reserve

        # check if stack is > 5
        self.check_height(player_obj, location)

        # check win condition
        if player_obj.get_captured_pieces() >= 6:
            return f"{player_obj.get_player_name()} Wins"

        # alternate turn
        self.set_turn(player_name)

        return "successfully moved"

    def check_height(self, player_obj, location):
        """method to check if stack of pieces is > 5 pieces tall: if so: capture bottom pieces that belong to
        the other player and/or reserve bottom pieces that belong to player in control of the stack
        :param player_obj: name of player who's in control of stack
        :type player_obj: Player
        :param location: coord to check height of
        :type location: tuple
        """
        for loc in self._board.get_full_board_list():
            if loc[0] == location:  # find coord
                while len(loc) > 6:  # stack taller than 5
                    bottom_piece = loc[1]
                    if bottom_piece == player_obj.get_player_color():
                        player_obj.set_reserve_pieces(1)
                    else:
                        player_obj.set_captured_pieces(1)
                    del loc[1]

    def show_pieces(self, loc):
        """shows pieces at a location on the board
        :param loc: coord to show
        :type loc: tuple
        :return: a list with pieces at that location, index 0 = base level, or "invalid location"
        :rtype: list or str
        """
        # validation check that coord exists
        val = self.validate_move(self._turn.get_player_name(), loc, (0, 0), 1)
        if val == "i_s_l":
            return "invalid location"

        # return list of pieces
        for space in self._board.get_full_board_list():
            if space[0] == loc:  # find loc
                return space[1:]

    def show_reserve(self, player_name):
        """show a count of pieces in that player's reserve
        :param player_name: name of player
        :type player_name: str
        :return: player's _reserve_pieces
        :rtype: int
        """
        return self.get_player_object(player_name).get_reserve_pieces()

    def show_captured(self, player_name):
        """show count of pieces in that player's captured
        :param player_name: name of player
        :type player_name: str
        :return: player's _captured_pieces
        :rtype: int
        """
        return self.get_player_object(player_name).get_captured_pieces()

    def get_player_object(self, player_name):
        """takes a player's name and returns the associated player object
        :param player_name: name of player
        :type player_name: str
        :return: player object
        :rtype: Player or bool
        """
        if player_name == self._player1.get_player_name():
            return self._player1
        elif player_name == self._player2.get_player_name():
            return self._player2
        else:
            return False  # could also return "not your turn"...?

    def get_turn(self):
        """get method for player_turn
        :return: player object whose turn it is
        :rtype: Player
        """
        return self._turn

    def set_turn(self, current_player_name):
        """set method for player_turn
        :param current_player_name: name of player
        :type current_player_name: str
        """
        if current_player_name == self._player1.get_player_name():
            self._turn = self._player2
        else:
            self._turn = self._player1

    def show_board(self):
        """shows board for current game"""
        self._board.show_board()


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

    # game = FocusGame(('PlayerA', 'R'), ('PlayerB', 'G'))
    # print(game._board.get_full_board_list())

    # # print(game._player1.get_player_color())
    # # print(game._player2.get_player_name())
    # # print(game._player2.get_captured_pieces())
    # print(game.move_piece("PlayerX", (0, 1), (0, 1), 1))  # wrong player
    # print(game.move_piece("PlayerA", (0, 0), (0, 1), 1))
    # # print(game.move_piece("PlayerA", (0, 0), (0, 1), 1))  # out of turn
    # print(game.move_piece("PlayerB", (0, 2), (0, 3), 1))
    # print(game.move_piece("PlayerA", (0, 1), (0, 4), 2))
    # print(game.move_piece("PlayerB", (0, 3), (0, 5), 2))
    # print(game.move_piece("PlayerA", (0, 4), (0, 1), 3))
    # print(game.move_piece("PlayerB", (0, 5), (0, 2), 3))
    # print(game.move_piece("PlayerA", (0, 1), (0, 1), 1))
    # print(game.move_piece("PlayerX", (0, 1), (0, 1), 1))  # wrong player
    # print(game.move_piece("PlayerB", (0, 1), (0, 2), 1))
    # print(game.get_turn().get_player_name())  # player name whose turn it is

    # print(game.get_turn().get_player_name())
    # print(game.move_piece("PlayerA", (0, 0), (0, 1), 1))
    # print(game.get_turn().get_player_name())
    # print(game.move_piece("PlayerB", (0, 2), (0, 3), 1))
    # print(game.get_turn().get_player_name())
    # print(game.move_piece("PlayerB", (0, 3), (0, 5), 2))
    # print(game.get_turn().get_player_name())
    # print(game.move_piece("PlayerA", (0, 1), (0, 4), 2))
    # print(game.move_piece("PlayerB", (0, 3), (0, 5), 2))

    # print(game.get_player_object("PlayerA"))
    # print(game.get_player_object("PlayerB"))
    # print(game.get_player_object("PlayerX"))

    # game._player1.set_reserve_pieces(1)
    # game._player1.set_reserve_pieces(1)
    # print(game.show_reserve("PlayerA"))
    # print(game.show_reserve("PlayerB"))
    # print(game.show_captured("PlayerA"))
    # print(game.show_captured("PlayerB"))
    # game._board.show_board()

    # print(game.show_pieces((0, 0)))
    # print(game.move_piece("PlayerA", (0, 1), (0, 0), 1))
    # print(game.show_pieces((0, 0)))
    # print(game.show_pieces((5, 5)))

    # print(game.move_piece("PlayerB", (0, 2), (0, 1), 1))  # not your turn
    # print(game.move_piece("PlayerA", (6, 8), (0, 1), 1))  # invalid loc
    # print(game.move_piece("PlayerA", (0, 0), (0, 4), 1))  # invalid loc
    # print(game.move_piece("PlayerA", (0, 1), (0, 3), 4))  # invalid loc
    # print(game.move_piece("PlayerA", (2, 1), (0, 3), 2))  # invalid loc
    # print(game.move_piece("PlayerA", (0, 0), (0, 1), 1))
    # print(game.move_piece("PlayerB", (0, 2), (0, 3), 1))
    # print(game.move_piece("PlayerA", (0, 1), (0, 3), 2))
    # print(game.move_piece("PlayerB", (0, 3), (0, 1), 2))  # invalid loc
    # print(game.move_piece("PlayerB", (1, 0), (1, 1), 1))
    # print(game.move_piece("PlayerA", (0, 3), (5, 3), 5))  # invalid num of pieces
    # print(game.validate_move("PlayerA", (0, 2), (0, 1), 1))  # invalid loc
    # print(game.validate_move("PlayerA", (0, 1), (0, 4), 3))  # invalid num of pieces

    # game._player1.set_reserve_pieces(1)
    # print(game.reserved_move("PlayerA", (0, 6)))  # invalid location
    # print(game.reserved_move("PlayerB", (0, 6)))  # not your turn
    # print(game.show_reserve("PlayerA"))
    # print(game.reserved_move("PlayerA", (0, 2)))
    # print(game.show_reserve("PlayerA"))
    # game.show_board()
    # print(game._board.get_full_board_list())

    # game._player1.set_reserve_pieces(1)
    # game.reserved_move("PlayerA", (0, 2))
    # print(game._board.get_full_board_list())

    # game.move_piece("PlayerA", (0, 1), (0, 0), 1)
    # print(game.show_pieces((0, 0)))

    # stack on (2, 2)
    # player1_obj = game.get_player_object("PlayerA")
    # print(game.show_reserve("PlayerA"))
    # print(game.show_reserve("PlayerB"))
    # print(game.show_captured("PlayerA"))
    # print(game.show_captured("PlayerB"))
    # print(game.move_piece("PlayerA", (2, 1), (2, 0), 1))
    # print(game.move_piece("PlayerB", (0, 3), (0, 2), 1))
    # print(game.move_piece("PlayerA", (2, 0), (2, 2), 2))
    # print(game.move_piece("PlayerB", (0, 2), (2, 2), 2))
    # print(game.move_piece("PlayerA", (1, 2), (2, 2), 1))
    # # print(game.move_piece("PlayerA", (2, 5), (2, 4), 1))
    # # print(game.move_piece("PlayerB", (4, 3), (4, 2), 1))
    # # print(game.move_piece("PlayerA", (2, 4), (2, 2), 2))
    # # game.check_height(player1_obj, (2, 2))
    # print(game.move_piece("PlayerB", (2, 3), (2, 2), 1))
    # print(game.move_piece("PlayerA", (3, 2), (2, 2), 1))
    # print(game.show_reserve("PlayerA"))
    # print(game.show_reserve("PlayerB"))
    # print(game.show_captured("PlayerA"))
    # print(game.show_captured("PlayerB"))
    # game.show_board()

    # player1_obj = game.get_player_object("PlayerA")
    # player1_obj.set_captured_pieces(5)
    # print(game.move_piece("PlayerA", (2, 1), (2, 0), 1))
    # player1_obj.set_captured_pieces(1)
    # print(game.move_piece("PlayerB", (0, 3), (0, 2), 1))
    # print(game.move_piece("PlayerA", (2, 0), (2, 2), 2))
    # game.show_board()

    # game = FocusGame(('PlayerA', 'R'), ('PlayerB', 'G'))
    # print(game.move_piece("PlayerA", (0, 0), (0, 1), 1))
    # print(game.move_piece("PlayerB", (0, 2), (0, 3), 1))
    # print(game.move_piece("PlayerA", (0, 1), (1, 0), 1))
    # print(game.show_pieces((0, 0)))
    # game.show_board()

    # READ ME
    # game = FocusGame(('PlayerA', 'R'), ('PlayerB', 'G'))
    # print(game.move_piece('PlayerA', (0, 0), (0, 1), 1))  # Returns message "successfully moved"
    # print(game.show_pieces((0, 1)))  # Returns ['R','R']
    # print(game.show_captured('PlayerA'))  # Returns 0
    # print(game.reserved_move('PlayerA', (0, 0)))  # Returns False, not per update (message "No pieces in reserve")
    # print(game.show_reserve('PlayerA'))  # Returns 0


if __name__ == '__main__':
    main()
