from rover import Constants as const
from rover.DirectionException import *

class Direction():
    def __init__(self, direction:int) -> None:
        if self.__isValidDirection(direction):
            self.direction = direction
        else:
            raise InvalidDirectionError()
        pass

    # TODO: Dictionary?
    def GetString(self):
        if self.IsNorth():
            return "N"
        if self.IsEast():
            return "E"
        if self.IsSouth():
            return "S"
        if self.IsWest():
            return "W"

    def TurnLeft(self):
        if self.IsNorth():
            self.direction = const.consts.WEST
        else:
            self.direction = self.direction - 1
    
    def TurnRight(self):
        if self.IsWest():
            self.direction = const.consts.NORTH
        else:
            self.direction = self.direction + 1

    def GetDirection(self):
        return self.direction

    def IsNorth(self):
        return self.direction == const.consts.NORTH

    def IsSouth(self):
        return self.direction == const.consts.SOUTH

    def IsWest(self):
        return self.direction == const.consts.WEST

    def IsEast(self):
        return self.direction == const.consts.EAST

    def __isValidDirection(self, direction):
        return (direction <= const.consts.WEST and direction >= const.consts.NORTH)