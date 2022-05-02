
from Throw import *

# A bowling frame consists of two throws
class Frame():

    def __init__(self, firstThrow: Throw, secondThrow: Throw) -> None:
        self.Throw1 = firstThrow
        self.Throw2 = secondThrow

    def isStrikeFrame(self):
        return self.Throw1.isStrike()

    def isSpareFrame(self):
        return self.Throw2.isSpare()

    def getFirstThrowScore(self):
        return self.Throw1.getPinsKnockedDown()
    
    def getSecondThrowScore(self):
        return self.Throw2.getPinsKnockedDown()