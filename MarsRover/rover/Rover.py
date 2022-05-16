import string
import rover.Constants as const
from rover.Mover import Mover
from rover.MoverException import *
from rover.RoverException import *


class Rover():
    def __init__(self, x:int=0, y:int=0, direction:int=const.consts.NORTH) -> None:
        if not self.__IsValidX(x):
            raise InvalidXCoordinateError("X coordinate must be between " + str(const.consts.MIN_X) + " and " + str(const.consts.MAX_X))
        if not self.__IsValidY(y):
            raise InvalidYCoordinateError("Y coordinate must be between " + str(const.consts.MIN_Y) + " and " + str(const.consts.MAX_Y))
            
        self.mover = Mover(x, y, direction)
        

    def Move(self, commandList:string):
        try:
            for command in commandList:
                currentPosition = self.mover.Move(command)

            return currentPosition
        except InvalidCommandError as exception:
            raise(exception)

    def GetLocation(self):
        return self.mover.GetLocation()

    def __IsValidX(self, x):
        if x <= const.consts.MAX_X and x >= const.consts.MIN_X:
            return True

    def __IsValidY(self, y):
        if y <= const.consts.MAX_Y and y >= const.consts.MIN_Y:
            return True