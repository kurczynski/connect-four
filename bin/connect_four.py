#!/usr/bin/env python

from enum import Enum, unique
from random import randint


@unique
class Checker(Enum):
    red = 0xff0000
    yellow = 0xffff00
    empty = -1


class GameBoard(object):
    ROWS = 6
    COLUMNS = 7
    CONNECT_COUNT = 4

    def __init__(self):
        # TODO: Clean this up.
        self.board = \
            [[Checker.empty for i in range(self.COLUMNS)] for j in
             range(self.ROWS)]

        self.player_color = None
        self.agent_color = None

    def print(self) -> None:
        """
        Prints the game board to stdout.
        """

        for row in reversed(self.board):
            print(row)

    def add_checker(self, checker: Checker, column: int) -> bool:
        """
        Adds a checker to the specified column.
        :param checker: the checker being placed into the game board.
        :param column: the column on the game board that the checker is being placed into.
        """

        for row in self.board:
            if row[column] is Checker.empty:
                row[column] = checker

                return True

        return False

    def check_winner(self) -> Checker:
        """
        Checks if the game board has a winner in its current state (i.e. the game is in a terminal state).
        :return: the checker that has won the game. If the game has not yet been won, returns None.
        """

        winner = self.check_vertical_win()
        if winner is not None:
            return winner

        winner = self.check_horizontal_win()
        if winner is not None:
            return winner

        winner = self.check_diagonal_win()
        if winner is not None:
            return winner

        return None

    def check_horizontal_win(self) -> Checker:
        """
        Checks if there is a horizontal win on the game board.
        :return: the checker that has won the game. If the game has not yet been won, returns None.
        """

        previous = None
        counter = 1

        for row in self.board:
            for space in row:
                if space == Checker.empty:
                    break
                elif space == previous:
                    counter += 1
                else:
                    counter = 1

                if counter == self.CONNECT_COUNT:
                    return space

                previous = space

        return None

    def check_vertical_win(self) -> Checker:
        """
        Checks if there is a vertical win on the game board.
        :return: the checker that has won the game. If the game has not yet been won, returns None.
        """

        previous = None
        counter = 1

        for column in range(self.COLUMNS - 1):
            for row in range(self.ROWS - 1):
                space = self.board[row][column]

                if space == Checker.empty:
                    break
                elif space == previous:
                    counter += 1
                else:
                    counter = 1

                if counter == self.CONNECT_COUNT:
                    return space

                previous = space

        return None

    def check_diagonal_win(self) -> Checker:
        """
        Checks if there is a diagonal win on the game board.
        :return: the checker that has won the game. If the game has not yet been won, returns None.
        """
        
        previous = None
        counter = 1

        for row in range(self.ROWS - 1):
            for column in range((self.COLUMNS - 1) - row):

                space = self.board[row][column]

                if space == Checker.empty:
                    break
                elif space == previous:
                    counter += 1
                else:
                    counter = 1

                if counter == self.CONNECT_COUNT:
                    return space

                previous = space
                row += 1

        return None


class UserInterface(object):
    @staticmethod
    def prompt_choice(prompt_string, max_choice, min_choice=1):
        choice = None

        while True:
            # TODO: Make sure input in numerical.
            choice = int(input(prompt_string))

            if max_choice >= choice >= min_choice:
                break
            else:
                print('Invalid choice.')

        return choice

    def get_checker_choice(self):
        prompt_string = (
            'Which color checker would you like to use?\n'
            '1) ' + Checker.yellow.name + '\n' +
            '2) ' + Checker.red.name + '\n')

        choice = self.prompt_choice(prompt_string, 2)

        return Checker.yellow if choice == 1 else Checker.red

    def get_column_choice(self):
        # TODO: Specify column range.
        prompt_string = 'Which column would you like to play?\n'

        choice = self.prompt_choice(prompt_string, GameBoard.COLUMNS)

        return choice


class Agent(object):
    pass


# def minimax(self):


class Node(object):
    def __init__(self, checker, column):
        self.children = []
        self.value = None
        self.game_board = GameBoard()
        self.game_board.add_checker(checker, column)

    def add_child(self, node):
        self.children.append(node)


class GameHandler(object):
    user_interface = None
    game_board = None

    human_checker = None
    agent_checker = None

    game_won = False

    # TODO: Add a random first turn method random.randint(0, 1)

    def __init__(self):
        print('Welcome to Connect Four!')

        self.game_board = GameBoard()
        self.user_interface = UserInterface()

        choice = self.user_interface.prompt_choice(
            'Which checker would you like to use?\n1) Red\n2) Yellow\n', 2)
        self.human_checker = Checker.red if choice == 1 else Checker.yellow

        self.agent_checker = Checker.yellow if self.human_checker is Checker.red else Checker.red

    def play_game(self):
        while not self.game_won:
            column = self.user_interface.get_column_choice()
            # FIXME: Make this column to index offset more clear.
            self.game_board.add_checker(self.human_checker, column - 1)

            self.game_board.print()

            # TODO: Agent's turn.


if __name__ == '__main__':
    game_board = GameBoard()

    game_board.check_diagonal_win()

    game_handler = GameHandler()

    game_handler.play_game()
