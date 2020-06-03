from cavegen import generateGrid, ROCK, WALL, FLOOR, print_grid


def neighborhood(row, col):
    return [
        (row - +1, col),
        (row + +1, col),
        (row, col - +1),
        (row, col + +1),
    ]


def get_adjacent(grid, row, col, visited):
    n = []
    for x, y in neighborhood(row, col):
        if not (0 <= x < len(grid) and 0 <= y < len(grid[x])):
            continue
        if (x, y) not in visited and (
            grid[x][y] is not ROCK and grid[x][y] is not WALL
        ):
            visited.append((x, y))
            n.append((x, y))
    return n


def measure(grid):
    visited = []
    areas = []
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if (x, y) not in visited:
                areas.append(bfs(grid, x, y, visited))
    areas = list(filter(lambda x: False if x is 0 else True, areas))
    return max(areas) / 2500


def bfs(grid, row, col, visited):
    visited.append((row, col))
    if grid[row][col] is ROCK or grid[row][col] is WALL:
        return 0
    s = 0
    adj = get_adjacent(grid, row, col, visited)
    for (x, y) in adj:
        s += bfs(grid, x, y, visited)
    return s + 1



