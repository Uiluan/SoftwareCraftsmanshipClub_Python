from Maze import Maze
from RecursiveMazeSolver import RecursiveMazeSolver

maze = Maze(20)
output = maze.GenerateMaze()
for elm in output:
    print(" ".join(elm))

solver = RecursiveMazeSolver(output)
solved = solver.SolveMaze()


print("\n")
for elm in solved:
    print(" ".join(elm))
