from Throw import *
from Frame import *


class BowlingScore():
    def __init__(self, scoreString) -> None:
        self.frameList = []
        for frame in scoreString.split():
            if frame == "X":
                # TODO: Create function
                firstThrow = Throw(ThrowType.STRIKE, 10)
                secondThrow = Throw(ThrowType.STRIKE, 0)
                self.frameList.append(Frame(firstThrow, secondThrow))
            elif "/" in frame:
                # TODO: Create function
                throwList = list(frame)
                for throwIndex, throw in enumerate(throwList):
                    if throw == "-":
                        throwList[throwIndex] = "0"
                firstThrow = Throw(ThrowType.STANDARD, int(throwList[0]))
                secondThrow = Throw(ThrowType.SPARE, 10 - int(throwList[0]))
                self.frameList.append(Frame(firstThrow, secondThrow))
            else:
                # TODO: Create function
                throwList = list(frame)
                for throwIndex, throw in enumerate(throwList):
                    if throw == "-":
                        throwList[throwIndex] = "0"
                firstThrow = Throw(ThrowType.STANDARD, int(throwList[0]))
                secondThrow = Throw(ThrowType.STANDARD, int(throwList[1]))
                self.frameList.append(Frame(firstThrow, secondThrow))

    def ScoreGame(self):
        score = 0
        for frameIndex, frame in enumerate(self.frameList):
            # TODO: bring index check to higher level. Maybe break scoring into single function to reduce depth
            if frame.isStrikeFrame():
                if frameIndex < 10:
                    score = score + self.__scoreStrike(frameIndex)
            elif frame.isSpareFrame():
                if frameIndex < 10:
                    score = score + self.__scoreSpare(frameIndex)
            else:
                if frameIndex < 10:
                    score = score + self.__scoreStandard(frameIndex)

        return score

    def __scoreStrike(self, strikeIndex):
        # TODO: Add exception for index >= 10
        score = self.frameList[strikeIndex].getFirstThrowScore()
        followingScore = self.frameList[strikeIndex + 1].getFirstThrowScore()
        if followingScore == 10:
            # Got a second strike, need to check first throw of next frame
            followingScore = followingScore + self.frameList[strikeIndex + 2].getFirstThrowScore()
        else:
            followingScore = followingScore + self.frameList[strikeIndex + 1].getSecondThrowScore()
        score = score + followingScore

        return score

    def __scoreSpare(self, spareIndex):
        # TODO: Add exception for index >= 10
        score = self.frameList[spareIndex].getFirstThrowScore() + self.frameList[spareIndex].getSecondThrowScore()
        score = score + self.frameList[spareIndex + 1].getFirstThrowScore()

        return score

    def __scoreStandard(self, standardIndex):
        # TODO: Add exception for index >= 10
        return self.frameList[standardIndex].getFirstThrowScore() + self.frameList[standardIndex].getSecondThrowScore()