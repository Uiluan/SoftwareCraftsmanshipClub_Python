GRID_MAX = 9
GRID_MIN = 0

class Coordinate():
    #TODO: Add exception for invalid coordinates
    def __init__(self, x:int, y:int) -> None:
        self.x = x
        self.y = y
        
    def MoveNorth(self):
        if self.y == GRID_MAX:
            self.y = GRID_MIN
        else:
            self.y = self.y + 1

    def MoveSouth(self):
        if self.y == GRID_MIN:
            self.y = GRID_MAX
        else:
            self.y = self.y - 1

    def MoveEast(self):
        if self.x == GRID_MAX:
            self.x = GRID_MIN
        else:
            self.x = self.x + 1

    def MoveWest(self):
        if self.x == GRID_MIN:
            self.x = GRID_MAX
        else:
            self.x = self.x - 1

    def GetCoordinates(self):
        return [self.x, self.y]

    def GetString(self):
        return str(self.x) + ":" + str(self.y)