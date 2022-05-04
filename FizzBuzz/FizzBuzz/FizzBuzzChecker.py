class FizzBuzzChecker():
    def __init__(self) -> None:
        pass

    def GetFizzBuzzResult(self, value):
        result = str(value)
        if self._isFizz(value):
            result = "Fizz"
        elif self._isBuzz(value):
            result = "Buzz"
        elif self._isFizzBuzz(value):
            result = "FizzBuzz"
        
        return result

    def _isFizz(self, value):
        if (value%3 == 0) and not (value%5 == 0):
            return True

    def _isBuzz(self, value):
        if (not value%3 == 0) and (value%5 == 0):
            return True

    def _isFizzBuzz(self, value):
        if (value %3 == 0) and (value%5 == 0):
            return True