# Name: Wes MacDonald
# Date: 11/22/2020
# Description:

import unittest
import FocusGame


class TestFocusGame(unittest.TestCase):
    """contains unit tests for FocusGame"""
    def test1G(self):
        game = FocusGame.FocusGame(("PlayerA", "R"), ("PlayerB", "G"))
        self.assertIs(game._player1.get_player_name(), "PlayerA")

    def test2G(self):
        game = FocusGame.FocusGame(("PlayerA", "R"), ("PlayerB", "G"))
        self.assertIs(game._player2.get_player_name(), "PlayerB")

    def test3G(self):
        game = FocusGame.FocusGame(("PlayerA", "R"), ("PlayerB", "G"))
        game.move_piece("PlayerA", (0, 0), (0, 1), 1)
        self.assertIs(game.get_turn().get_player_name(), "PlayerB")

    def test4G(self):
        game = FocusGame.FocusGame(("PlayerA", "R"), ("PlayerB", "G"))
        game.move_piece("PlayerB", (0, 2), (0, 3), 1)
        self.assertIs(game.get_turn().get_player_name(), "PlayerA")

    def test5G(self):
        game = FocusGame.FocusGame(("PlayerA", "R"), ("PlayerB", "G"))
        self.assertEqual(game.move_piece("PlayerA", (0, 0), (0, 1), 1), "successfully moved")

    def test6G(self):
        game = FocusGame.FocusGame(("PlayerA", "R"), ("PlayerB", "G"))
        game.move_piece("PlayerA", (0, 0), (0, 1), 1)
        self.assertEqual(game.move_piece("PlayerB", (0, 1), (0, 0), 2), False)

    def test7G(self):
        game = FocusGame.FocusGame(("PlayerA", "R"), ("PlayerB", "G"))
        self.assertEqual(game.move_piece("PlayerB", (0, 1), (0, 0), 2), False)

    def test8G(self):
        game = FocusGame.FocusGame(("PlayerA", "R"), ("PlayerB", "G"))
        game.move_piece("PlayerA", (0, 0), (0, 1), 1)
        self.assertEqual(game.move_piece("PlayerA", (0, 1), (0, 0), 2), False)

    def test9G(self):
        game = FocusGame.FocusGame(("PlayerA", "R"), ("PlayerB", "G"))
        self.assertEqual(game.move_piece("PlayerA", (6, 8), (0, 1), 1), False)

    def test10G(self):
        game = FocusGame.FocusGame(("PlayerA", "R"), ("PlayerB", "G"))
        self.assertEqual(game.move_piece("PlayerA", (0, 0), (0, 4), 1), False)

    def test11G(self):
        game = FocusGame.FocusGame(("PlayerA", "R"), ("PlayerB", "G"))
        self.assertEqual(game.move_piece("PlayerA", (0, 1), (0, 3), 4), False)

    def test12G(self):
        game = FocusGame.FocusGame(("PlayerA", "R"), ("PlayerB", "G"))
        self.assertEqual(game.move_piece("PlayerA", (2, 1), (0, 3), 2), False)

    def test13G(self):
        game = FocusGame.FocusGame(("PlayerA", "R"), ("PlayerB", "G"))
        game.move_piece("PlayerA", (0, 0), (0, 1), 1)
        game.move_piece("PlayerB", (0, 2), (0, 3), 1)
        game.move_piece("PlayerA", (0, 1), (0, 3), 2)
        self.assertEqual(game.move_piece("PlayerB", (0, 3), (0, 1), 2), False)

    def test14G(self):
        game = FocusGame.FocusGame(("PlayerA", "R"), ("PlayerB", "G"))
        game.move_piece("PlayerA", (0, 0), (0, 1), 1)
        game.move_piece("PlayerB", (0, 2), (0, 3), 1)
        game.move_piece("PlayerA", (0, 1), (0, 3), 2)
        self.assertEqual(game.move_piece("PlayerB", (1, 0), (1, 1), 1), "successfully moved")

    def test15G(self):
        game = FocusGame.FocusGame(("PlayerA", "R"), ("PlayerB", "G"))
        game.move_piece("PlayerA", (0, 0), (0, 1), 1)
        game.move_piece("PlayerB", (0, 2), (0, 3), 1)
        game.move_piece("PlayerA", (0, 1), (0, 3), 2)
        game.move_piece("PlayerB", (1, 0), (1, 1), 1)
        self.assertEqual(game.move_piece("PlayerA", (0, 3), (5, 3), 5), False)

    def test16G(self):
        game = FocusGame.FocusGame(("PlayerA", "R"), ("PlayerB", "G"))
        game.move_piece("PlayerA", (0, 0), (0, 1), 1)
        game.move_piece("PlayerB", (0, 2), (0, 3), 1)
        game.move_piece("PlayerA", (0, 1), (0, 3), 2)
        game.move_piece("PlayerB", (1, 0), (1, 1), 1)
        self.assertEqual(game.move_piece("PlayerA", (0, 3), (4, 3), 4), "successfully moved")

    def test17G(self):
        game = FocusGame.FocusGame(("PlayerA", "R"), ("PlayerB", "G"))
        game.move_piece("PlayerA", (0, 0), (0, 1), 1)
        game.move_piece("PlayerB", (0, 2), (0, 3), 1)
        game.move_piece("PlayerA", (0, 1), (0, 3), 2)
        game.move_piece("PlayerB", (1, 0), (1, 1), 1)
        self.assertEqual(game.move_piece("PlayerA", (0, 3), (0, 0), 3), "successfully moved")

    def test18G(self):
        game = FocusGame.FocusGame(("PlayerA", "R"), ("PlayerB", "G"))
        self.assertEqual(game.move_piece("PlayerA", (0, 2), (0, 1), 1), False)

    def test19G(self):
        game = FocusGame.FocusGame(("PlayerA", "R"), ("PlayerB", "G"))
        self.assertEqual(game.move_piece("PlayerA", (0, 4), (0, 1), 1), False)

    def test20G(self):
        game = FocusGame.FocusGame(("PlayerA", "R"), ("PlayerB", "G"))
        self.assertEqual(game.move_piece("PlayerA", (0, 4), (0, 1), 3), False)

    def test21G(self):
        game = FocusGame.FocusGame(("PlayerA", "R"), ("PlayerB", "G"))
        self.assertEqual(game.reserved_move("PlayerA", (0, 4)), False)

    def test22G(self):
        game = FocusGame.FocusGame(("PlayerA", "R"), ("PlayerB", "G"))
        game._player1.set_reserve_pieces(1)
        self.assertEqual(game.reserved_move("PlayerA", (0, 4)), "successfully moved")

    def test23G(self):
        game = FocusGame.FocusGame(("PlayerA", "R"), ("PlayerB", "G"))
        game._player1.set_reserve_pieces(1)
        self.assertEqual(game.reserved_move("PlayerA", (10, 7)), False)

    def test24G(self):
        game = FocusGame.FocusGame(("PlayerA", "R"), ("PlayerB", "G"))
        game._player1.set_reserve_pieces(1)
        self.assertEqual(game.reserved_move("PlayerA", (4, -4)), False)

    def test25G(self):
        game = FocusGame.FocusGame(("PlayerA", "R"), ("PlayerB", "G"))
        game._player1.set_reserve_pieces(1)
        self.assertEqual(game.reserved_move("PlayerB", (0, 4)), False)

    def test26G(self):
        game = FocusGame.FocusGame(("PlayerA", "R"), ("PlayerB", "G"))
        start_board = [[(0, 0), 'R'], [(0, 1), 'R'], [(0, 2), 'G'], [(0, 3), 'G'], [(0, 4), 'R'], [(0, 5), 'R'],
                       [(1, 0), 'G'], [(1, 1), 'G'], [(1, 2), 'R'], [(1, 3), 'R'], [(1, 4), 'G'], [(1, 5), 'G'],
                       [(2, 0), 'R'], [(2, 1), 'R'], [(2, 2), 'G'], [(2, 3), 'G'], [(2, 4), 'R'], [(2, 5), 'R'],
                       [(3, 0), 'G'], [(3, 1), 'G'], [(3, 2), 'R'], [(3, 3), 'R'], [(3, 4), 'G'], [(3, 5), 'G'],
                       [(4, 0), 'R'], [(4, 1), 'R'], [(4, 2), 'G'], [(4, 3), 'G'], [(4, 4), 'R'], [(4, 5), 'R'],
                       [(5, 0), 'G'], [(5, 1), 'G'], [(5, 2), 'R'], [(5, 3), 'R'], [(5, 4), 'G'], [(5, 5), 'G']]
        game.move_piece("PlayerA", (0, 0), (0, 1), 1)
        self.assertNotEqual(game._board.get_full_board_list(), start_board)

    def test27G(self):
        game = FocusGame.FocusGame(("PlayerA", "R"), ("PlayerB", "G"))
        end_board = [[(0, 0),], [(0, 1), 'R', 'R'], [(0, 2), 'G'], [(0, 3), 'G'], [(0, 4), 'R'], [(0, 5), 'R'],
                       [(1, 0), 'G'], [(1, 1), 'G'], [(1, 2), 'R'], [(1, 3), 'R'], [(1, 4), 'G'], [(1, 5), 'G'],
                       [(2, 0), 'R'], [(2, 1), 'R'], [(2, 2), 'G'], [(2, 3), 'G'], [(2, 4), 'R'], [(2, 5), 'R'],
                       [(3, 0), 'G'], [(3, 1), 'G'], [(3, 2), 'R'], [(3, 3), 'R'], [(3, 4), 'G'], [(3, 5), 'G'],
                       [(4, 0), 'R'], [(4, 1), 'R'], [(4, 2), 'G'], [(4, 3), 'G'], [(4, 4), 'R'], [(4, 5), 'R'],
                       [(5, 0), 'G'], [(5, 1), 'G'], [(5, 2), 'R'], [(5, 3), 'R'], [(5, 4), 'G'], [(5, 5), 'G']]
        game.move_piece("PlayerA", (0, 0), (0, 1), 1)
        self.assertEqual(game._board.get_full_board_list(), end_board)

    def test28G(self):
        game = FocusGame.FocusGame(("PlayerA", "R"), ("PlayerB", "G"))
        game._player1.set_reserve_pieces(1)
        end_board = [[(0, 0), 'R'], [(0, 1), 'R', 'R'], [(0, 2), 'G'], [(0, 3), 'G'], [(0, 4), 'R'], [(0, 5), 'R'],
                       [(1, 0), 'G'], [(1, 1), 'G'], [(1, 2), 'R'], [(1, 3), 'R'], [(1, 4), 'G'], [(1, 5), 'G'],
                       [(2, 0), 'R'], [(2, 1), 'R'], [(2, 2), 'G'], [(2, 3), 'G'], [(2, 4), 'R'], [(2, 5), 'R'],
                       [(3, 0), 'G'], [(3, 1), 'G'], [(3, 2), 'R'], [(3, 3), 'R'], [(3, 4), 'G'], [(3, 5), 'G'],
                       [(4, 0), 'R'], [(4, 1), 'R'], [(4, 2), 'G'], [(4, 3), 'G'], [(4, 4), 'R'], [(4, 5), 'R'],
                       [(5, 0), 'G'], [(5, 1), 'G'], [(5, 2), 'R'], [(5, 3), 'R'], [(5, 4), 'G'], [(5, 5), 'G']]
        game.reserved_move("PlayerA", (0, 1))
        self.assertEqual(game._board.get_full_board_list(), end_board)

    def test29G(self):
        game = FocusGame.FocusGame(("PlayerA", "R"), ("PlayerB", "G"))
        game.move_piece("PlayerA", (2, 1), (2, 0), 1)
        game.move_piece("PlayerB", (2, 2), (1, 2), 1)
        game.move_piece("PlayerA", (2, 0), (0, 0), 2)
        game.move_piece("PlayerB", (1, 2), (3, 2), 2)
        game.move_piece("PlayerA", (0, 0), (0, 3), 3)
        game.move_piece("PlayerB", (3, 2), (3, 5), 3)
        game.move_piece("PlayerA", (0, 3), (2, 3), 2)
        game.move_piece("PlayerB", (3, 4), (3, 3), 1)
        game.move_piece("PlayerA", (0, 1), (0, 2), 1)
        game.move_piece("PlayerB", (3, 5), (0, 5), 3)
        game.move_piece("PlayerA", (2, 3), (5, 3), 3)
        game.move_piece("PlayerB", (0, 5), (4, 5), 4)
        game.move_piece("PlayerA", (5, 3), (2, 3), 3)
        game.move_piece("PlayerB", (4, 5), (4, 0), 5)
        game.move_piece("PlayerA", (2, 3), (5, 3), 3)
        game.move_piece("PlayerB", (3, 0), (4, 0), 1)
        game.move_piece("PlayerA", (5, 2), (5, 3), 1)
        game.move_piece("PlayerB", (5, 4), (5, 3), 1)
        game.move_piece("PlayerA", (4, 1), (4, 0), 1)
        game.move_piece("PlayerB", (3, 3), (5, 3), 2)
        game.move_piece("PlayerA", (4, 0), (4, 4), 4)
        game.move_piece("PlayerB", (1, 4), (2, 4), 1)
        game.move_piece("PlayerA", (4, 0), (5, 0), 1)
        self.assertEqual(game.move_piece("PlayerB", (2, 4), (4, 4), 2), "PlayerB Wins")

    def test1_check_height(self):
        game = FocusGame.FocusGame(("PlayerA", "R"), ("PlayerB", "G"))
        game.move_piece("PlayerA", (2, 1), (2, 0), 1)
        self.assertEqual(game.show_reserve("PlayerA"), 0)

    def test2_check_height(self):
        game = FocusGame.FocusGame(("PlayerA", "R"), ("PlayerB", "G"))
        game.move_piece("PlayerA", (2, 1), (2, 0), 1)
        self.assertEqual(game.show_captured("PlayerA"), 0)

    def test3_check_height(self):
        game = FocusGame.FocusGame(("PlayerA", "R"), ("PlayerB", "G"))
        game.move_piece("PlayerA", (2, 1), (2, 0), 1)
        self.assertEqual(game.show_reserve("PlayerB"), 0)

    def test4_check_height(self):
        game = FocusGame.FocusGame(("PlayerA", "R"), ("PlayerB", "G"))
        game.move_piece("PlayerA", (2, 1), (2, 0), 1)
        self.assertEqual(game.show_captured("PlayerB"), 0)

    def test5_check_height(self):
        game = FocusGame.FocusGame(("PlayerA", "R"), ("PlayerB", "G"))
        game.move_piece("PlayerA", (2, 1), (2, 0), 1)
        game.move_piece("PlayerB", (0, 3), (0, 2), 1)
        game.move_piece("PlayerA", (2, 0), (2, 2), 2)
        game.move_piece("PlayerB", (0, 2), (2, 2), 2)
        game.move_piece("PlayerA", (1, 2), (2, 2), 1)
        self.assertEqual(game.show_captured("PlayerA"), 1)

    def test6_check_height(self):
        game = FocusGame.FocusGame(("PlayerA", "R"), ("PlayerB", "G"))
        game.move_piece("PlayerA", (2, 1), (2, 0), 1)
        game.move_piece("PlayerB", (0, 3), (0, 2), 1)
        game.move_piece("PlayerA", (2, 0), (2, 2), 2)
        game.move_piece("PlayerB", (0, 2), (2, 2), 2)
        game.move_piece("PlayerA", (1, 2), (2, 2), 1)
        self.assertEqual(game.show_reserve("PlayerA"), 0)

    def test7_check_height(self):
        game = FocusGame.FocusGame(("PlayerA", "R"), ("PlayerB", "G"))
        game.move_piece("PlayerA", (2, 1), (2, 0), 1)
        game.move_piece("PlayerB", (0, 3), (0, 2), 1)
        game.move_piece("PlayerA", (2, 0), (2, 2), 2)
        game.move_piece("PlayerB", (0, 2), (2, 2), 2)
        game.move_piece("PlayerA", (1, 2), (2, 2), 1)
        game.move_piece("PlayerB", (2, 3), (2, 2), 1)
        self.assertEqual(game.show_captured("PlayerB"), 1)

    def test8_check_height(self):
        game = FocusGame.FocusGame(("PlayerA", "R"), ("PlayerB", "G"))
        game.move_piece("PlayerA", (2, 1), (2, 0), 1)
        game.move_piece("PlayerB", (0, 3), (0, 2), 1)
        game.move_piece("PlayerA", (2, 0), (2, 2), 2)
        game.move_piece("PlayerB", (0, 2), (2, 2), 2)
        game.move_piece("PlayerA", (1, 2), (2, 2), 1)
        game.move_piece("PlayerB", (2, 3), (2, 2), 1)
        game.move_piece("PlayerA", (3, 2), (2, 2), 1)
        self.assertEqual(game.show_reserve("PlayerA"), 1)

    def test9_check_height(self):
        game = FocusGame.FocusGame(("PlayerA", "R"), ("PlayerB", "G"))
        game.move_piece("PlayerA", (2, 1), (2, 0), 1)
        game.move_piece("PlayerB", (0, 3), (0, 2), 1)
        game.move_piece("PlayerA", (2, 0), (2, 2), 2)
        game.move_piece("PlayerB", (0, 2), (2, 2), 2)
        game.move_piece("PlayerA", (1, 2), (2, 2), 1)
        game.move_piece("PlayerB", (2, 3), (2, 2), 1)
        game.move_piece("PlayerA", (3, 2), (2, 2), 1)
        self.assertEqual(game.show_captured("PlayerA"), 1)

    def test10_check_height(self):
        game = FocusGame.FocusGame(("PlayerA", "R"), ("PlayerB", "G"))
        game.move_piece("PlayerA", (2, 1), (2, 0), 1)
        game.move_piece("PlayerB", (0, 3), (0, 2), 1)
        game.move_piece("PlayerA", (2, 0), (2, 2), 2)
        game.move_piece("PlayerB", (0, 2), (2, 2), 2)
        game.move_piece("PlayerA", (1, 2), (2, 2), 1)
        game.move_piece("PlayerB", (2, 3), (2, 2), 1)
        game.move_piece("PlayerA", (3, 2), (2, 2), 1)
        game.move_piece("PlayerB", (1, 1), (1, 0), 1)
        game.move_piece("PlayerA", (2, 5), (2, 4), 1)
        game.move_piece("PlayerB", (3, 1), (2, 1), 1)
        game.move_piece("PlayerA", (2, 4), (2, 2), 2)
        self.assertEqual(game.show_captured("PlayerA"), 3)

    def test11_check_height(self):
        game = FocusGame.FocusGame(("PlayerA", "R"), ("PlayerB", "G"))
        game.move_piece("PlayerA", (2, 1), (2, 0), 1)
        game.move_piece("PlayerB", (0, 3), (0, 2), 1)
        game.move_piece("PlayerA", (2, 0), (2, 2), 2)
        game.move_piece("PlayerB", (0, 2), (2, 2), 2)
        game.move_piece("PlayerA", (1, 2), (2, 2), 1)
        game.move_piece("PlayerB", (2, 3), (2, 2), 1)
        game.move_piece("PlayerA", (3, 2), (2, 2), 1)
        game.move_piece("PlayerB", (1, 1), (1, 0), 1)
        game.move_piece("PlayerA", (2, 5), (2, 4), 1)
        game.move_piece("PlayerB", (3, 1), (2, 1), 1)
        game.move_piece("PlayerA", (2, 4), (2, 2), 2)
        game.move_piece("PlayerB", (2, 1), (2, 2), 1)
        # print(game.show_board())
        self.assertEqual(game.show_captured("PlayerB"), 2)

    def test1(self):
        game = FocusGame.FocusGame(("PlA-ah", "Red"), ("Ble-ah", "Gre"))
        game.move_piece("PlA-ah", (0, 0), (0, 1), 1)
        # game.show_board()
        self.assertEqual(game.move_piece("Ble-ah", (0, 2), (0, 3), 1), "successfully moved")


if __name__ == "__main__":
    unittest.main()
