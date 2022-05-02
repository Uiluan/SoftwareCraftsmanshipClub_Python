from Maze import Maze
from RecursiveMazeSolver import RecursiveMazeSolver

def printArray(array):
    for elm in array:
        print(" ".join(elm))

def testOne():
    maze = [ [ 'S' , '0' , '1' ], [ '1' , '0' , '1' ], [ '1' , '0' , 'E' ] ]

    print("\nMaze:")
    printArray(maze)

    mazeSolver = RecursiveMazeSolver(maze)
    solvedMaze = mazeSolver.SolveMaze()

    print("\nSolved Maze:")
    printArray(solvedMaze)

def testTwo():
    maze = [ ['S','0','0','0','0'], ['1','1','1','1','0'], ['0','0','0','1','0' ], ['0','1','0','1','0' ], 
    ['0','1','0','0','0'], ['0','1','1','1','1'], ['0','1','0','0','0'], ['0','1','1','1','1'], ['0','0','0','0','1'], 
    ['0','1','0','1','1'], ['1','1','0','0','E',] ]

    print("\nMaze:")
    printArray(maze)

    mazeSolver = RecursiveMazeSolver(maze)
    solvedMaze = mazeSolver.SolveMaze()

    print("\nSolved Maze:")
    printArray(solvedMaze)

def testRandom():
    maze = Maze(5)
    randomMaze = maze.GenerateMaze()

    print("\nMaze:")
    printArray(randomMaze)

    mazeSolver = RecursiveMazeSolver(randomMaze)
    solvedMaze = mazeSolver.SolveMaze()

    print("\nSolved Maze:")
    printArray(solvedMaze)

testOne()
testTwo()
testRandom()