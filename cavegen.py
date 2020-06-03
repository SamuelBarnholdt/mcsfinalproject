import random

WALL = 2
ROCK = 1
FLOOR = 0


def generateGrid(r, n, T, M):
    rowCount, columnCount = 50, 50
    grid = [[0 for i in range(50)] for i in range(50)]
    generateRandomRocks(grid, rowCount, columnCount, r)

    while n > 0:
        for row in range(rowCount):
            for col in range(columnCount):
                if (grid[row][col] is not ROCK) and (
                    countNeighborRocks(grid, row, col, M, rowCount, columnCount) > T
                ):
                    grid[row][col] = ROCK
        n -= 1
    #print_grid(grid)
    rockToWall(grid, rowCount, columnCount)
    return grid


# finished
def rockToWall(grid, rowDim, colDim):
    for row in range(rowDim):
        for col in range(colDim):
            if grid[row][col] is ROCK:
                for cell in checkNeighborHood(grid, row, col, 1):
                    if cell is FLOOR:
                        grid[row][col] = WALL
                        break


def checkNeighborHood(grid, row, col, M):
    nh = []
    for x, y in moore_neighborhood(row, col, M):
        if not (0 <= x < len(grid) and 0 <= y < len(grid[x])):
            # out of bounds
            continue
        nh.append(grid[x][y])
    return nh


def moore_neighborhood(row, col, M):
    mn = []
    for i in range(M):
        mn.append((row - (i + 1), col))
        mn.append((row + (i + 1), col))
        mn.append((row, col - (i + 1)))
        mn.append((row, col + (i + 1)))
        mn.append((row - (i + 1), col - (i + 1)))
        mn.append((row - (i + 1), col + (i + 1)))
        mn.append((row + (i + 1), col - (i + 1)))
        mn.append((row + (i + 1), col + (i + 1)))
    return mn


def countNeighborRocks(grid, row, col, M, rowCount, columnCount):
    count = 0
    for cell in checkNeighborHood(grid, row, col, M):
        count += cell
    return count


def print_grid(grid):
    print("\033[2J\033[;H")
    count = 0
    for row in grid:
        for element in row:
            if element is 0:
                print(".", end=""),
            if element is 1:
                print("*", end=""),
            if element is 2:
                print("W", end=""),
        print("")
    print(count)


def generateRandomRocks(grid, rowDim, colDim, r):
    rockCount = rowDim * colDim
    numRocks = int(rockCount * r)
    rList = []

    for i in range(rockCount):
        rList.append(i)

    shuffle(rList)
    for cell in range(numRocks):
        rI = int(rList[cell] / rowDim)
        cI = int(rList[cell] % colDim)
        grid[rI][cI] = ROCK
    #print_grid(grid)


def shuffle(lst):
    highestIndex = len(lst)
    for i in reversed(range(highestIndex)):
        swap = random.randint(0, i)
        tmp = lst[i]
        lst[i] = lst[swap]
        lst[swap] = tmp


print(generateGrid(0.5, 2, 5, 1))


print_grid(generateGrid(0.3, 1, 10, 1))
