#  File: numberPath.py
#  Description: Find the path that sums to the target sum
#  Student's Name: Charles Lybrand
#  Student's UT EID: cbl652
#  Course Name: CS 313E 
#  Unique Number: 51915
#
#  Date Created: 04/07/2017
#  Date Last Modified: 04/08/2017


class State():
    '''
    object that holds the state of the grid and other important variables
    '''
    def __init__(self, grid, his, sr, sc, val, sum):
        self.grid = grid
        self.pathHistory = his
        self.startRow = sr
        self.startCol = sc
        self.value = val
        self.sum = sum
        
    def __str__(self):
        '''
        Print a formated grid and all of the variables
        '''
        gridStr = "   Grid:"
        for row in self.grid:
            gridStr += "\n".ljust(7)
            for col in row:
                gridStr += str(col).ljust(5)
        gridStr += "\n   history: " + str(self.pathHistory)
        gridStr += "\n   start point: (%s, %s)" % (str(self.startRow), str(self.startCol))
        gridStr += "\n   sum so far: " + str(self.sum)
        return gridStr
    
    
def isValid(grid, gridRows, gridColsl, posRow, posCol):
    '''
    Tests whether moving to a proposed position is legal
    '''
    # check if in bounds
    if( (posRow < 0 or posRow >= gridRows) or (posCol < 0 or posCol >= gridColsl) ):
        return False
    # check if already visited
    if(grid[posRow][posCol] == None):
        return False
    # position must be valid
    return True


def copyGrid(grid):
    '''
    Make a copy of a grid
    '''
    newGrid = []
    for row in grid:
        newRow = []
        for col in row:
            newRow.append(col)
        newGrid.append(newRow)
    return newGrid


def solve(state, targetValue, gridRows, gridCols, endRow, endCol):
    '''
    Solve recursively uses depth-first search to find the path
    '''
    
    print()
    print("Problem is now:")
    print(state)
    print()
    print("Is this a goal state?")
    
    # if the sum is the target and we're at the end point, return the history
    if(state.sum == targetValue and state.startRow == endRow and state.startCol == endCol):
        print("Solution Found!")
        return state.pathHistory
    
    else:
        # if the target has been exceeded, return None to backtrack
        if(state.sum > targetValue):
            print("No. Target exceeded:  abandoning path")
            return None

        # check if can move right
        print("No.  Can I move right?")
        if(isValid(state.grid, gridRows, gridCols, state.startRow, state.startCol + 1)):
            print("Yes!")
            # calculate all new variables that will go into the recursive solve call
            newCol = state.startCol + 1
            newGrid = copyGrid(state.grid)
            newVal = newGrid[state.startRow][newCol]
            newGrid[state.startRow][newCol] = None
            newHist = state.pathHistory[:]
            newHist.append(newVal)
            newSum = state.sum + newVal
            newState = State(newGrid, newHist, state.startRow, newCol, newVal, newSum)
            result = solve(newState, targetValue, gridRows, gridCols, endRow, endCol)
            if result != None:
                return result

        # check if can move up
        print("No.  Can I move up?")
        if(isValid(state.grid, gridRows, gridCols, state.startRow - 1, state.startCol)):
            print("Yes!")
            # calculate all new variables that will go into the recursive solve call
            newRow = state.startRow - 1
            newGrid = copyGrid(state.grid)
            newVal = newGrid[newRow][state.startCol]
            newGrid[newRow][state.startCol] = None
            newHist = state.pathHistory[:]
            newHist.append(newVal)
            newSum = state.sum + newVal
            newState = State(newGrid, newHist, newRow, state.startCol, newVal, newSum)
            result = solve(newState, targetValue, gridRows, gridCols, endRow, endCol)
            if result != None:
                return result

        # check if can move down
        print("No.  Can I move down?")
        if(isValid(state.grid, gridRows, gridCols, state.startRow + 1, state.startCol)):
            print("Yes!")
            # calculate all new variables that will go into the recursive solve call
            newRow = state.startRow + 1
            newGrid = copyGrid(state.grid)
            newVal = newGrid[newRow][state.startCol]
            newGrid[newRow][state.startCol] = None
            newHist = state.pathHistory[:]
            newHist.append(newVal)
            newSum = state.sum + newVal
            newState = State(newGrid, newHist, newRow, state.startCol, newVal, newSum)
            result = solve(newState, targetValue, gridRows, gridCols, endRow, endCol)
            if result != None:
                return result

        # check if can move left
        print("No.  Can I move left?")
        if(isValid(state.grid, gridRows, gridCols, state.startRow, state.startCol - 1)):
            print("Yes!")
            # calculate all new variables that will go into the recursive solve call
            newCol = state.startCol - 1
            newGrid = copyGrid(state.grid)
            newVal = newGrid[state.startRow][newCol]
            newGrid[state.startRow][newCol] = None
            newHist = state.pathHistory[:]
            newHist.append(newVal)
            newSum = state.sum + newVal
            newState = State(newGrid, newHist, state.startRow, newCol, newVal, newSum)
            result = solve(newState, targetValue, gridRows, gridCols, endRow, endCol)
            if result != None:
                return result


        # if nothing worked, return None to backtrack
        return None

    
def main():
    
    # read in the file
    infile = open("pathdata.txt", "r")
    # read in the first line and save all the variables
    targetValue, gridRows, gridCols, startRow, startCol, endRow, endCol = list(map(int, infile.readline().split()))
    # format the rest of the grid
    grid = [list(map(int, line.split())) for line in infile ]
    # close the file
    infile.close()
    
    # create the first "State"
    val = grid[startRow][startCol]
    grid[startRow][startCol] = None
    startState = State(grid, [val], startRow, startCol, val, val)
    # print the starting state
    # print(startState)
    
    # solve the number path
    print(solve(startState, targetValue, gridRows, gridCols, endRow, endCol))
    print()
    
if __name__ == "__main__":
    main()

