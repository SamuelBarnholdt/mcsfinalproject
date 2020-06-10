from cavegen import generateGrid, ROCK, WALL, FLOOR, print_grid
from measure import get_adjacent


def measure_hills(grid):
    visited = []
    areas = []
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if (x, y) not in visited:
                areas.append(bfs_hills(grid, x, y, visited))
    areas = list(filter(lambda x: False if x is 0 else True, areas))
    return max(areas) / (len(grid) * len(grid[0]) * 4)


def bfs_hills(grid, row, col, visited):
    visited.append((row, col))
    if grid[row][col] is ROCK or grid[row][col] is WALL:
        return 0
    s = 0
    adj = get_adjacent(grid, row, col, visited)
    for (x, y) in adj:
        s += bfs_hills(grid, x, y, visited)

    return s + (1 if grid[row][col] is FLOOR else grid[row][col] - 1)
