import unittest
from unittest import TestCase

from bin.connect_four import GameBoard, Checker


class TestGameBoard(TestCase):
    def test_add_checker(self):
        self.fail()

    def test_check_winner(self):
        game_board = GameBoard()

        # Check horizontal wins.
        for i in range(GameBoard.CONNECT_COUNT):
            game_board.add_checker(Checker.red, i)

        self.assertEqual(game_board.check_winner(), Checker.red)

    def test_check_diagonal_win(self):
        game_board = GameBoard()

        for i in range(GameBoard.CONNECT_COUNT):
            for j in range(i + 1):
                game_board.add_checker(Checker.red, i)

        game_board.print()

        self.assertEqual(game_board.check_diagonal_win(), Checker.red)

if __name__ == '__main__':
    unittest.main()
