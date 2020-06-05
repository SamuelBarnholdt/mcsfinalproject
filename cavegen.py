import random

import matplotlib.pyplot as plt
from matplotlib import colors

u_prob = 0.2

UPHILL = 3
WALL = 2
ROCK = 1
FLOOR = 0


def generateGrid(r, n, T, M):
    rowCount, columnCount = 50, 50
    grid = [[0 for i in range(50)] for i in range(50)]
    #print(len(grid[0]))
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
    makeHills(grid)
    return grid

def makeHills(grid):
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            # Catching div by zero errors since they are bound to happen for this kind of sum.
            try:
                # Taking 1 over the sum of the neighbors will give open areas a higher prob of having hills,
                # since it will divide by a smaller sum.
                s = 1/((sum(checkNeighborHood(grid,row,col,1))))
            except ZeroDivisionError:
                #print('zero')
                # If the sum happens to be zero the prob of a hill is equal to having only rock neighbors - 1/8
                s = 0.125
            if(grid[row][col] == FLOOR) and (random.random() < s):
                grid[row][col] = UPHILL

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
    for x, y in (
        (row - 1, col),
        (row + 1, col),
        (row, col - 1),
        (row, col + 1),
        (row - 1, col - 1),
        (row - 1, col + 1),
        (row + 1, col - 1),
        (row + 1, col + 1),
    ):
        if not (0 <= x < len(grid) and 0 <= y < len(grid[x])):
            # out of bounds
            continue
        nh.append(grid[x][y])
    return nh


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


#print(generateGrid(0.5, 10, 5, 1))
#print_grid(generateGrid(0.5, 1, 5, 1))
cmap = colors.ListedColormap(['grey', 'white', 'red', 'green'])
bounds=[0,1,2,3,4]
norm = colors.BoundaryNorm(bounds, cmap.N)
plt.imshow(generateGrid(0.5, 4, 13, 1), cmap = cmap, norm = norm)
plt.colorbar()
plt.show()