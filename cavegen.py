import random

import matplotlib.pyplot as plt
from matplotlib import colors 

u_prob = 0.2

UPHILL3 = 5
UPHILL2 = 4
UPHILL1 = 3
WALL = 2
ROCK = 1
FLOOR = 0


def generateGrid(r, n, T, M):
    rowCount, columnCount = 40, 40
    grid = [[0 for i in range(rowCount)] for i in range(columnCount)]
    #print(len(grid[0]))
    generateRandomRocks(grid, rowCount, columnCount, r)

    while n > 0:
        for row in range(rowCount):
            for col in range(columnCount):
                if (grid[row][col] is not ROCK) and (
                    countNeighborRocks(grid, row, col, M, rowCount, columnCount) > T
                ):
                    grid[row][col] = ROCK
                makeHills(grid, row, col, M)
        n -= 1
    #print_grid(grid)
    rockToWall(grid, rowCount, columnCount)
    return grid

def makeHills(grid, row, col, M = 1):
    # Worlds hackiest solution:    
        # Catching div by zero errors since they are bound to happen for this kind of sum.
    try:
        # Taking 1 over the sum of the neighbors will give open areas a higher prob of having hills,
        # since it will divide by a smaller sum.
        s = 1/((sum(checkNeighborHood(grid,row,col,M))))
    except ZeroDivisionError:
        #print('zero')
        # If the sum happens to be zero the prob of a hill is high, since it's only floor around.
        s = 0.75
    if(grid[row][col] == FLOOR) and (random.random() < s):
        grid[row][col] = UPHILL1
    elif(grid[row][col] == UPHILL1) and (random.random() < s):
        grid[row][col] = UPHILL2
    elif(grid[row][col] == UPHILL2) and (random.random() < s):
        grid[row][col] = UPHILL3

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


cmap = colors.ListedColormap(['thistle', 'teal', 'black', 'plum', 'violet', 'fuchsia'])
#cmap = colors.ListedColormap(['white', 'black','black','white','white','white'])
bounds=[0,1,2,3,4,5,6]
norm = colors.BoundaryNorm(bounds, cmap.N)
plt.imshow(generateGrid(0.5, 4, 13, 1), cmap = cmap, norm = norm)
plt.colorbar()
plt.show()