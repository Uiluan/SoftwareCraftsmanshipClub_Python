from rover import Constants as const
from rover.DirectionException import *

class Direction():
    def __init__(self, direction:int) -> None:
        if self.__isValidDirection(direction):
            self.direction = direction
        else:
            raise InvalidDirectionError()
        pass

    def GetString(self):
        match self.direction:
            case const.consts.NORTH:
                return "N"
            case const.consts.EAST:
                return "E"
            case const.consts.SOUTH:
                return "S"
            case const.consts.WEST:
                return "W"

    def TurnLeft(self):
        if self.direction == const.consts.NORTH:
            self.direction = const.consts.WEST
        else:
            self.direction = self.direction - 1
    
    def TurnRight(self):
        if self.direction == const.consts.WEST:
            self.direction = const.consts.NORTH
        else:
            self.direction = self.direction + 1

    def GetDirection(self):
        return self.direction
        

    def __isValidDirection(self, direction):
        return (direction <= const.consts.WEST and direction >= const.consts.NORTH)