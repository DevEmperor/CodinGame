"""
This code is under the terms of the Apapche 2.0 license,
following all clarifications stated here: https://www.apache.org/licenses/LICENSE-2.0

Created by Jannis Zahn
"""

def get_adjacent(g, x, y):  # returns a list of al neighbors of a tile
    a = {}
    if x > 0 and y > 0: a[(x - 1, y - 1)] = g[y - 1][x - 1]  # top-left
    if y > 0: a[(x, y - 1)] = g[y - 1][x]  # top-mid
    if x < 29 and y > 0: a[(x + 1, y - 1)] = g[y - 1][x + 1]  # top-right
    if x < 29: a[(x + 1, y)] = g[y][x + 1]  # right-mid
    if x < 29 and y < 15: a[(x + 1, y + 1)] = g[y + 1][x + 1]  # bottom-right
    if y < 15: a[(x, y + 1)] = g[y + 1][x]  # bottom-mid
    if x > 0 and y < 15: a[(x - 1, y + 1)] = g[y + 1][x - 1]  # bottom-left
    if x > 0: a[(x - 1, y)] = g[y][x - 1]  # left-mid
    return a


# game loop
while True:
    grid = [input().split() for _ in [0]*16]  # reads the grid from stdio

    # check if all are unknown
    if all(cell == "?" for line in grid for cell in line):
        print("0 0")
        continue

    """
    Rule 1: If a tile has the same amount of hidden tiles around it
    as unflagged bombs remaining around it
    then all the hidden tiles are bombs
    """
    mine = None
    for y in range(16):
        for x in range(30):
            try:
                if int(grid[y][x]) >= sum(v == "?" for v in get_adjacent(grid, x, y).values()):
                    mine = [i[0] for i in get_adjacent(grid, x, y).items() if i[1] == "?"][0]
                    break
            except ValueError:
                continue
        else:
            continue
        break


    """
    Rule 2: If a tile has the same amount of flags around it as the number  on the square,
    then all remaining hidden tiles around it are not bombs
    """
    free = None
    for y in range(16):
        for x in range(30):
            try:
                if int(grid[y][x]) == sum(v not in "?." and not v.isdigit() for v in get_adjacent(grid, x, y).values()):
                    free = [i[0] for i in get_adjacent(grid, x, y).items() if i[1] == "?"][0]
                    break
            except ValueError:
                continue
        else:
            continue
        break

    print((" ".join(free) if free else "") + (" ".join(mine) if mine else ""))

import random

grid = [[random.randint(0, 9) for __ in range(30)] for _ in range(16)]
print(*grid, sep="\n")
print([v for v in get_adjacent(grid, 10, 10)])
