import string

from rover.Location import Location
from rover.MoverException import InvalidCommandError

class Mover():
    def __init__(self, x:int, y:int, direction:string) -> None:
        self.location = Location(x, y, direction)

    def Move(self, command:string):
        if str(command).upper() == "L":
            self.location.TurnLeft()
        elif str(command).upper() == "R":
            self.location.TurnRight()
        elif str(command).upper() == "M":
            self.location.Move()
        else:
            raise InvalidCommandError()
        
        return self.location.GetLocation()

    def GetLocationString(self):
        return self.location.GetString()

    def GetLocation(self):
        return self.location.GetLocation()
