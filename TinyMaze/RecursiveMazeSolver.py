from msilib.schema import CompLocator


class RecursiveMazeSolver():
    def __init__(self, maze) -> None:
        self.maze = maze
        self.wasHere = [[False for i in range(0, len(self.maze))] for j in range(0, len(self.maze[0]))]
        self.correctPath = [[0 for i in range(0, len(self.maze))] for j in range(0, len(self.maze[0]))]

    def SolveMaze(self):
        startRow, startColumn = self.__findStart()
        self.endX, self.endY = self.__findEnd()

        if self.__solveRecursively(startRow, startColumn+1) == True:
            for rowIndex in range(0, len(self.correctPath)):
                for columnIndex in range(0, len(self.correctPath[0])):
                    if self.correctPath[rowIndex][columnIndex] == True:
                        self.maze[rowIndex][columnIndex] = 'x'
            return self.maze

    # Assumes start is always on left hand side of maze
    def __findStart(self):
        rowIndex = 0
        for row in self.maze:
            if row[0] == 'S':
                return rowIndex, 0
            rowIndex = rowIndex + 1

    # Assumes end is always on right hand side of maze
    def __findEnd(self):
        rowIndex = 0
        for row in self.maze:
            if row[-1] == 'E':
                return rowIndex, len(row)-1
            rowIndex = rowIndex + 1

    def __solveRecursively(self, x, y):
        if self.maze[x][y] == 'E':
            return True

        test = self.maze[x][y]
        if self.maze[x][y] == '1' or self.wasHere[x][y] == True:
            return False

        self.wasHere[x][y] = True

        if x != 0:
            if self.__solveRecursively(x - 1, y):
                self.correctPath[x][y] = True
                return True

        if x != len(self.maze[0]) - 1:
            if self.__solveRecursively(x + 1, y):
                self.correctPath[x][y] = True
                return True

        if y != 0:
            if self.__solveRecursively(x, y - 1):
                self.correctPath[x][y] = True
                return True

        if y != len(self.maze) - 1:
            if self.__solveRecursively(x, y + 1):
                self.correctPath[x][y] = True
                return True

        return False