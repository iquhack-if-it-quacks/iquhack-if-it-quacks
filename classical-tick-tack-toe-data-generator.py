import random

import numpy as np


winners = {}


def has_winner(grid):
    for i in range(3):
        sum = grid[i * 3] + grid[i * 3 + 1] + grid[i * 3 + 2]
        if (sum == 3 or sum == -3): return sum / 3

    for i in range(3):
        sum = grid[i] + grid[i + 3] + grid[i + 6]
        if (sum == 3 or sum == -3): return sum / 3

    sum = grid[0] + grid[4] + grid[8]
    if (sum == 3 or sum == -3): return sum / 3
    sum = grid[2] + grid[4] + grid[6]
    if (sum == 3 or sum == -3): return sum / 3

    return 0


def is_player_winner(player, grid):
    winner = has_winner(grid)
    if winner == 0: return 0
    if winner == 1 and player == 0: return 1  # player X won, he gets 1
    if winner == -1 and player == 1: return 1  # player O won, he gets 1
    return -1


def is_full(grid):
    for v in grid:
        if v == 0: return False
    return True


def get_grid_hash(grid):
    hash = ""
    for v in grid:
        hash += "x" if v == 1 else ("o" if v == -1 else "-")
    return hash


def get_available_actions(grid):
    actions = []
    for i, v in enumerate(grid):
        if v == 0:
            actions.append(i)
    return actions


count = 0


def get_winner(grid, turn):
    global count
    count += 1
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


def displayGrid(grid):
  for i in range(2, -1, -1):
    str = ""
    for j in range(3):
      v = grid[i * 3 + j]for a, b in zip(pred, test_labels):
    print(a, b)
      str += ("x" if v == 1 else ("o" if v == -1 else "-"))
    print(str)


data = []

for i in range(1000):
    grid = np.zeros(9)
    turn = random.choice((-1, 1))
    while has_winner(grid) == 0 and len(get_available_actions(grid)):
        data.append((get_grid_hash(grid), get_winner(grid, turn) == turn))
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
#     print('\nAvailable moves:', get_available_actions(grid))
#     cellStr = input("enter your move: ")
#     cell = int(cellStr)
#     if(grid[cell] != 0):
#         print(cellStr, ' is taken! Try again')
#         continue
#     grid[cell] = 1
#     hash = get_grid_hash(grid)
#     print('You:')
#     displayGrid(grid)
#     winner = has_winner(grid)
#     if winner != 0:
#         print('*** YOU WON ***')
#         done = True
#         break
#     if is_full(grid):
#         done = True
#         print('DRAW')
#         break
#
#     my_action = get_available_actions(grid)[0]
#     is_winning = False
#     for action in get_available_actions(grid):
#         cgrid = grid.copy()
#         cgrid[action] = -1
#         if get_winner(cgrid, 1) == -1:
#             my_action = action
#             is_winning = True
#
#     if not is_winning:
#         for action in get_available_actions(grid):
#             cgrid = grid.copy()
#             cgrid[action] = -1
#             if get_winner(cgrid, 1) == 0:
#                 my_action = action
#
#     grid[my_action] = -1
#     hash = get_grid_hash(grid)
#     print("Algorithm:")
#     displayGrid(grid)
#     winner = has_winner(grid)
#     if winner != 0:
#         print('--- YOU LOST ---')
#         done = True
#         break
