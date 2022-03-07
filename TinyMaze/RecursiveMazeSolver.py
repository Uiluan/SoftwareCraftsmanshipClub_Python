from msilib.schema import CompLocator


class RecursiveMazeSolver():
    def __init__(self, maze) -> None:
        self.maze = maze
        self.wasHere = [[False for i in range(0, len(self.maze[0]))] for j in range(0, len(self.maze))]
        self.correctPath = [[False for i in range(0, len(self.maze[0]))] for j in range(0, len(self.maze))]

    def SolveMaze(self):
        startRow, startColumn = self.__findStart()
        self.endX, self.endY = self.__findEnd()

        #TODO: Enhance to catch unsolvable mazes
        if self.__solveRecursively(startRow, startColumn+1) == True:
            self.__addCorrectPathToMaze()
            return self.maze

    def __findStart(self):
        # Assumes start is always on left hand side of maze
        for rowIndex in range(0, len(self.maze)):
            if self.maze[rowIndex][0] == 'S':
                return rowIndex, 0
    
    def __findEnd(self):
        # Assumes end is always on right hand side of maze
        for rowIndex in range(0, len(self.maze)):
            if self.maze[rowIndex][-1] == 'E':
                return rowIndex, len(self.maze[0]) - 1

    def __addCorrectPathToMaze(self):
        for rowIndex in range(0, len(self.correctPath)):
            for columnIndex in range(0, len(self.correctPath[0])):
                self.__replaceStartPosition(rowIndex, columnIndex)
                self.__replaceEndPosition(rowIndex, columnIndex)
                self.__replacePath(rowIndex, columnIndex)
                
    def __replaceStartPosition(self, row, column):
        if self.maze[row][column] == 'S':
            self.maze[row][column] = 'x'

    def __replaceEndPosition(self, row, column):
        if self.maze[row][column] == 'E':
            self.maze[row][column] = 'x'

    def __replacePath(self, row, column):
        if self.correctPath[row][column] == True:
            self.maze[row][column] = 'x'

    def __solveRecursively(self, row, column):
        if self.maze[row][column] == 'E':
            return True

        if self.maze[row][column] == '1' or self.wasHere[row][column] == True:
            return False

        self.wasHere[row][column] = True

        if row != 0:
            if self.__solveRecursively(row - 1, column):
                self.correctPath[row][column] = True
                return True

        if row != len(self.maze) - 1:
            if self.__solveRecursively(row + 1, column):
                self.correctPath[row][column] = True
                return True

        if column != 0:
            if self.__solveRecursively(row, column - 1):
                self.correctPath[row][column] = True
                return True

        if column != len(self.maze[0]) - 1:
            if self.__solveRecursively(row, column + 1):
                self.correctPath[row][column] = True
                return True

        return False
