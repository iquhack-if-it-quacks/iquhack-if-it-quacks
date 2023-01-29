def has_winner(grid):
    for i in range(3):
        sum = grid[i * 3] + grid[i * 3 + 1] + grid[i * 3 + 2]
        if sum == 3 or sum == -3:
            return sum / 3
    for i in range(3):
        sum = grid[i] + grid[i + 3] + grid[i + 6]
        if sum == 3 or sum == -3:
            return sum / 3
    sum = grid[0] + grid[4] + grid[8]
    if sum == 3 or sum == -3:
        return sum / 3
    sum = grid[2] + grid[4] + grid[6]
    if sum == 3 or sum == -3:
        return sum / 3
    return 0


def is_player_winner(player, grid):
    winner = has_winner(grid)
    if winner == 0: return 0
    if winner == 1 and player == 0: return 1  # player X won, he gets 1
    if winner == -1 and player == 1: return 1  # player O won, he gets 1
    return -1


def is_full(grid):
    for v in grid:
        if v == 0:
            return False
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


def displayGrid(grid):
    for i in range(2, -1, -1):
        text = ""
        for j in range(3):
            v = grid[i * 3 + j]
            text += ("x" if v == 1 else ("o" if v == -1 else "-"))
        print(text)


def neutralize_grid(grid, turn):
    return [int(x * turn) for x in grid]
