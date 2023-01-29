import random

import numpy as np
from helper import *

winners = {}


def get_winner(grid, turn):
    hsh = get_grid_hash(grid), turn
    if hsh in winners:
        return winners[hsh]
    tmp = has_winner(grid)
    if tmp != 0:
        winners[hsh] = tmp
        return tmp
    if len(get_available_actions(grid)) == 0:
        winners[hsh] = 0
        return 0
    any_draw = False
    for cell in get_available_actions(grid):
        cgrid = grid.copy()
        cgrid[cell] = turn
        tmp = get_winner(cgrid, -turn)
        if tmp == turn:
            winners[hsh] = turn
            return turn
        if tmp == 0:
            any_draw = True
    winners[hsh] = -turn
    if any_draw:
        return 0
    return -turn


data = []

for i in range(1000):
    grid = np.zeros(9)
    turn = random.choice((-1, 1))
    while has_winner(grid) == 0 and len(get_available_actions(grid)):
        ngrid = neutralize_grid(get_grid_hash(grid), turn)
        nwinner = get_winner(grid, turn) == turn
        data.append((ngrid, nwinner))
        action = random.choice(get_available_actions(grid))
        grid[action] = turn
        turn *= -1

for grid, winner in data:
    print(grid, winner)

# print("Play by entering the number of cell to put X in.")
# done = False
# grid = np.zeros(9)
#
# while not done:
#   print('\nAvailable moves:', get_available_actions(grid))
#   cellStr = input("enter your move: ")
#   cell = int(cellStr)
#   if(grid[cell] != 0):
#     print(cellStr, ' is taken! Try again')
#     continue
#   grid[cell] = 1
#   hash = get_grid_hash(grid)
#   print('You:')
#   displayGrid(grid)
#   winner = has_winner(grid)
#   if winner != 0:
#     print('*** YOU WON ***')
#     done = True
#     break
#   if is_full(grid):
#     done = True
#     print('DRAW')
#     break
#
#   my_action = get_available_actions(grid)[0]
#   is_winning = False
#   for action in get_available_actions(grid):
#       cgrid = grid.copy()
#       cgrid[action] = -1
#       if get_winner(cgrid, 1) == -1:
#         my_action = action
#         is_winning = True
#
#   if not is_winning:
#       for action in get_available_actions(grid):
#           cgrid = grid.copy()
#           cgrid[action] = -1
#           if get_winner(cgrid, 1) == 0:
#             my_action = action
#
#   grid[my_action] = -1
#   hash = get_grid_hash(grid)
#   print("Algorithm:")
#   displayGrid(grid)
#   winner = has_winner(grid)
#   if winner != 0:
#     print('--- YOU LOST ---')
#     done = True
#     break
