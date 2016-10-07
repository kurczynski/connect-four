import unittest
from unittest import TestCase

from bin.connect_four import GameBoard, Checker, Direction


class TestGameBoard(TestCase):
    def test_add_checker(self):
        self.fail()

    def test_get_winner(self):
        game_board = GameBoard()

        # Check horizontal wins.
        for i in range(GameBoard.CONNECT_COUNT):
            game_board.add_checker(Checker.red, i)

        self.assertEqual(game_board.check_win(Direction.horizontal), Checker.red)


if __name__ == '__main__':
    unittest.main()


