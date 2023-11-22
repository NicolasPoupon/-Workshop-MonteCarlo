#!/usr/bin/env python3

import random
from puissance4 import Puissance4

def mock_input(prompt):
    while True:
        try:
            player_move = int(input(prompt))
            if 0 < player_move <= 7:
                return player_move
            else:
                print("Write a number between 1 - 7")
        except ValueError:
            print("Write a number between 1 - 7")

def main():
    game = Puissance4()
    while not game.is_finished():
        game.print_info()
        player = mock_input("Your turn: ")
        game._drop_piece(player, 'o')
        ia = random.randint(0, 6)
        print("IA turn: ", ia)
        game.play(ia)
    game.print_winner()

if __name__ == '__main__':
    main()
