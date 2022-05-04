from random import Random, random

NORTH = 0
EAST  = 1
SOUTH = 2
WEST  = 3
MINPOSITIONX = 0
MAXPOSITIONX = 9
MINPOSITIONY = 0
MAXPOSITIONY = 9

class Rover():
    def __init__(self) -> None:
        # "land" the rover at a random position within the grid
        randomizer = Random()
        self.__SetPosition(randomizer.randint(MINPOSITIONX,MAXPOSITIONX), randomizer.randint(MINPOSITIONY,MAXPOSITIONY))
        self.__SetDirection(randomizer.randint(NORTH, WEST))

    def Execute(self, commands):
        if self.__IsValidCommand(commands):
            commandList = list(commands)
            for currentCommand in commandList:
                self.__ExecuteCommand(currentCommand)
            return True #TODO: Investigate change to exception
        else:
            return False

    def GetPositionAndDirection(self):
        return self.__GetPositionX(), self.__GetPositionY(), self.__GetDirectionText()

# Private helpers
    def __GetPositionX(self):
        return self.xPosition

    def __GetPositionY(self):
        return self.yPosition

    def __SetPosition(self, x, y):
        if x >= MINPOSITIONX and x <= MAXPOSITIONX:
            self.xPosition = x
        if y >= MINPOSITIONY and y <= MAXPOSITIONY:
            self.yPosition = y

    def __GetDirection(self):
        return self.direction

    def __GetDirectionText(self):
        return {
            NORTH: "N",
            EAST : "E",
            SOUTH: "S",
            WEST : "W"
        }[self.direction]

    def __SetDirection(self, dir):
        if dir < NORTH:
            self.direction = WEST
        elif dir > WEST:
            self.direction = NORTH
        else:
            self.direction = dir

    def __VerifyCommand(self, command): #TODO: I have a VerifyCommand and an IsValidCommand, investigate if duplication
        if command == "M" or command == "L" or command == "R":
            return True
        else:
            return False

    def __TurnLeft(self):
        self.__SetDirection(self.__GetDirection()-1)

    def __TurnRight(self):
        self.__SetDirection(self.__GetDirection()+1)

    def __Move(self):
        if self.__GetDirection() == NORTH:
            self.__MoveNorth()
        elif self.__GetDirection() == EAST:
            self.__MoveEast()
        elif self.__GetDirection() == SOUTH:
            self.__MoveSouth()
        elif self.__GetDirection() == WEST:
            self.__MoveWest()

    def __MoveNorth(self):
        if self.__GetPositionY() < MAXPOSITIONY:
            self.__SetPosition(self.__GetPositionX(), self.__GetPositionY()+1)
        else:
            self.__SetPosition(self.__GetPositionX(), MINPOSITIONY)

    def __MoveEast(self):
        if self.__GetPositionX() < MAXPOSITIONX:
            self.__SetPosition(self.__GetPositionX()+1, self.__GetPositionY())
        else:
            self.__SetPosition(MINPOSITIONX, self.__GetPositionY())

    def __MoveSouth(self):
        if self.__GetPositionY() > MINPOSITIONY:
            self.__SetPosition(self.__GetPositionX(), self.__GetPositionY()-1)
        else:
            self.__SetPosition(self.__GetPositionX(), MAXPOSITIONY)

    def __MoveWest(self):
        if self.__GetPositionX() > MINPOSITIONX:
            self.__SetPosition(self.__GetPositionX()-1, self.__GetPositionY())
        else:
            self.__SetPosition(MAXPOSITIONX, self.__GetPositionY())

    def __ExecuteCommand(self, command):
        command = command.upper()
        if self.__VerifyCommand(command):
            if command == 'L':
                self.__TurnLeft()
            elif command == 'R':
                self.__TurnRight()
            elif command == 'M':
                self.__Move()
            return True #TODO: Investigate change to exception
        else:
            return False

    def __IsValidCommand(self, command):
        allowedCommands = set('MRL')
        commands = command.upper()
        if set(commands) <= allowedCommands:
            return True
        else:
            return False