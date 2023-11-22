#!/usr/bin/env python3

import os
import copy
import random

class Puissance4:
    def __init__(self):
        self.grid = [[' ' for _ in range(7)] for _ in range(6)]
        self.turn = 1

    def print_info(self):
        print('\n\n- Turn ' + str(self.turn) + ' -')
        for row in self.grid:
            print('| ' + ' | '.join(row) + ' |')
        print('\n')

    def play(self, ia_move):
        self._drop_piece(ia_move, 'x')
        self.turn += 1

    def _drop_piece(self, column, piece):
        for row in reversed(self.grid):
            if row[column-1] == ' ':
                row[column-1] = piece
                return
        print("Column is full")

    def _check_finished(self):
        for row in range(6):
            for col in range(7):
                if self.grid[row][col] != ' ' and self._check_victory(row, col):
                    self.winner = self.grid[row][col]
                    return True
        if all(self.grid[0][col] != ' ' for col in range(7)):
            self.winner = 'Nobody'
            return True
        return False

    def _check_victory(self, row, col):
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
        for dr, dc in directions:
            if self._check_line(row, col, dr, dc):
                return True
        return False

    def _check_line(self, row, col, dr, dc):
        piece = self.grid[row][col]
        for n in range(1, 4):
            r, c = row + dr*n, col + dc*n
            if r not in range(6) or c not in range(7) or self.grid[r][c] != piece:
                return False
        return True

    def is_finished(self):
        return self._check_finished()

    def print_winner(self):
        self.print_info()
        if self.winner:
            print(f"{self.winner} wins!")
        else:
            print("It's a tie!")

    def _check_win_in_one(self, player):
        for column in range(7):
            if self.grid[0][column] == ' ':
                row = self._find_empty_row(column)
                if row is not None:
                    self.grid[row][column] = player
                    if self._check_victory(row, column):
                        self.grid[row][column] = ' '
                        return column
                    self.grid[row][column] = ' '
        return -1

    def _find_empty_row(self, column):
        for row in range(5, -1, -1):
            if self.grid[row][column] == ' ':
                return row
        return None

    def _find_best_move(self, player):
        winning_move = self.check_win_in_one(player)
        if winning_move != -1:
            return winning_move
        opponent = 'x' if player == 'o' else 'o'
        blocking_move = self.check_win_in_one(opponent)
        if blocking_move != -1:
            return blocking_move

        possible_moves = [col for col in range(7) if self.grid[0][col] == ' ']
        return random.choice(possible_moves)

    # Faites vos exercices ici
