import unittest
from unittest import TestCase

from bin.connect_four import GameBoard, Checker, Direction


class TestGameBoard(TestCase):
	TEST_CHECKER = Checker.red

	def setUp(self):
		self.game_board = GameBoard()

	def test_add_checker(self):
		self.game_board.add_checker(self.TEST_CHECKER, 0)
		self.assertEqual(self.game_board.board[GameBoard.ROWS - 1][0], self.TEST_CHECKER)

		self.game_board.clear_board()

		for i in range(GameBoard.ROWS):
			self.game_board.add_checker(self.TEST_CHECKER, 0)

		self.assertEqual(self.game_board.board[0][0], self.TEST_CHECKER)

		self.game_board.clear_board()

		self.game_board.add_checker(self.TEST_CHECKER, self.game_board.COLUMNS - 1)
		self.assertEqual(
			self.game_board.board[self.game_board.ROWS - 1][self.game_board.COLUMNS - 1], self.TEST_CHECKER)

		self.game_board.clear_board()

		for i in range(GameBoard.ROWS):
			self.game_board.add_checker(self.TEST_CHECKER, self.game_board.COLUMNS - 1)

		self.assertEqual(self.game_board.board[0][self.game_board.COLUMNS - 1], self.TEST_CHECKER)

	def test_check_all_wins(self):
		pass

	def text_diagonal_left_win(self):
		pass

	def text_diagonal_right_win(self):
		pass

	def test_vertical_win(self):
		for i in range(GameBoard.CONNECT_COUNT):
			self.game_board.add_checker(self.TEST_CHECKER, 0)

		self.assertEqual(self.game_board.check_all_wins(), self.TEST_CHECKER)
		self.game_board.clear_board()

	def test_horizontal_win(self):
		for i in range(GameBoard.CONNECT_COUNT):
			self.game_board.add_checker(self.TEST_CHECKER, i)

		self.assertEqual(self.game_board.check_all_wins(), self.TEST_CHECKER)
		self.game_board.clear_board()


if __name__ == '__main__':
	unittest.main()
