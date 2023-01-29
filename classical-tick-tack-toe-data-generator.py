import random

import numpy as np
from helper import *

winners = {}


def get_winner(grid, turn):
    hsh = get_grid_hash(grid), turn
    if hsh in winners:
        return winners[hsh]
    tmp = int(has_winner(grid))
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
    if any_draw:
        winners[hsh] = 0
        return 0
    winners[hsh] = -turn
    return -turn


data = []

for i in range(1000):
    grid = np.zeros(9)
    turn = random.choice((-1, 1))
    while has_winner(grid) == 0 and len(get_available_actions(grid)):
        ngrid = neutralize_grid(grid, turn)
        nwinner = get_winner(ngrid, 1)
        data.append((ngrid, nwinner))
        action = random.choice(get_available_actions(grid))
        grid[action] = turn
        turn *= -1
    # ngrid = neutralize_grid(grid, turn)
    # nwinner = get_winner(grid, turn) * turn
    # data.append((ngrid, nwinner))


for grid, winner in data:
    print(grid, winner)
