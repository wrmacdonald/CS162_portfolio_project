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
        self.assertEqual(game.move_piece("PlayerB", (0, 1), (0, 0), 2), "invalid location")

    def test7G(self):
        game = FocusGame.FocusGame(("PlayerA", "R"), ("PlayerB", "G"))
        self.assertEqual(game.move_piece("PlayerB", (0, 1), (0, 0), 2), "not your turn")

    def test8G(self):
        game = FocusGame.FocusGame(("PlayerA", "R"), ("PlayerB", "G"))
        game.move_piece("PlayerA", (0, 0), (0, 1), 1)
        self.assertEqual(game.move_piece("PlayerA", (0, 1), (0, 0), 2), "not your turn")


if __name__ == "__main__":
    unittest.main()
