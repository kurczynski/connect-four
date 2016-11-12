import unittest
from unittest import TestCase

from bin.connect_four import GameBoard, Checker, Direction


class TestGameBoard(TestCase):
    def setUp(self):
        self.game_board = GameBoard()

    def test_add_checker(self):
        self.fail()

    def test_check_all_wins(self):
        pass

    def text_diagonal_left_win(self):
        pass

    def text_diagonal_right_win(self):
        pass

    def test_vertical_win(self):
        for i in range(GameBoard.CONNECT_COUNT):
            self.game_board.add_checker(Checker.red, 0)

        self.assertEqual(self.game_board.check_all_wins(), Checker.red)
        self.game_board.clear_board()

    def test_horizontal_win(self):
        for i in range(GameBoard.CONNECT_COUNT):
            self.game_board.add_checker(Checker.red, i)

        self.assertEqual(self.game_board.check_all_wins(), Checker.red)
        self.game_board.clear_board()

if __name__ == '__main__':
    unittest.main()


