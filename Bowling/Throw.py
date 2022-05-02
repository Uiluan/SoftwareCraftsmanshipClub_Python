
from enum import Enum

class ThrowType(Enum):
    STANDARD = 0
    STRIKE = 1
    SPARE = 2

class Throw():
    def __init__(self, throwType: ThrowType, pinsKnockedDown: int) -> None:
        self.type = throwType
        self.pins = pinsKnockedDown

    def isStrike(self):
        return self.type == ThrowType.STRIKE

    def isSpare(self):
        return self.type == ThrowType.SPARE

    def isStandard(self):
        return self.type == ThrowType.STANDARD

    def getPinsKnockedDown(self):
        return self.pins