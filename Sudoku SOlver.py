def printGrid(grid):
        for i in range(9):
                for j in range(9):
                        print(grid[i][j]," ", end="")
                print("\n")


def findEmptyPlace(grid, l):
        for row in range(1, 10):
                for col in range(1, 10):
                        if grid[row][col]==0:
                                l[0]=row
                                l[1]=col
                                return True
        return False

def rowCheck(grid, row, col, num):
        for i in range(9):
                if grid[row][i]==num:
                        return False
        return True

def colCheck(grid, row, col, num):
        for i in range(9):
                if grid[i][col]==num:
                        return False
        return True

def boxCheck(grid, row, col, num):
        for i in range(3):
                for j in range(3):
                        if grid[i+row][j+col]==num:
                                return False
        return True
        
def checkAll(grid, row, col, num):
        return rowCheck(grid, row, col, num) and colCheck(grid, row, col, num) and boxCheck(grid, row, col, num)

def solveGrid(grid):
        l=[0,0]
        if not (findEmptyPlace(grid, l)):
                return True
        row=l[0]
        col=l[1]

        for num in range(1, 10):
                if checkAll(grid, row, col, num):
                        grid[row][col]=num

                        if solveGrid(grid):
                                return True
                        
                        grid[row][col]=0
        return False


grid=[[3,0,6,5,0,8,4,0,0], 
          [5,2,0,0,0,0,0,0,0], 
          [0,8,7,0,0,0,0,3,1], 
          [0,0,3,0,1,0,0,8,0], 
          [9,0,0,8,6,3,0,0,5], 
          [0,5,0,0,9,0,6,0,0], 
          [1,3,0,0,0,0,2,5,0], 
          [0,0,0,0,0,0,0,7,4], 
          [0,0,5,2,0,6,3,0,0]] 
if (solveGrid(grid)):
        printGrid(grid)
else:
        print("Not possible")