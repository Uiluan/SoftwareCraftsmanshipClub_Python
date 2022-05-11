from rover.Direction import Direction
from rover.Coordinate import Coordinate
import rover.Constants as const

class Location():
    #TODO Make paramters optional? Default to 0:0:N
    def __init__(self, x:int, y:int, direction:int) -> None:
        self.direction = Direction(direction)
        self.coordinate = Coordinate(x, y)

    def TurnLeft(self):
        self.direction.TurnLeft()

    def TurnRight(self):
        self.direction.TurnRight()

    def Move(self):
        if self.direction.IsNorth():
            self.coordinate.MoveNorth()
        elif self.direction.IsWest():
            self.coordinate.MoveWest()
        elif self.direction.IsSouth():
            self.coordinate.MoveSouth()
        elif self.direction.IsEast():
            self.coordinate.MoveEast()

    def GetLocation(self):
        x, y = self.coordinate.GetCoordinates()
        dir = self.direction.GetDirection()
        return [x, y, dir]

    def GetString(self):
        return self.coordinate.GetString() + ":" + self.direction.GetString()