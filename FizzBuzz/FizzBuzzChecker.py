class FizzBuzzChecker():
    def __init__(self) -> None:
        pass

    def GetFizzBuzzResult(self, value):
        if (value%3 == 0) and not (value%5 == 0):
            return "Fizz"
        if (not value%3 == 0) and (value%5 == 0):
            return "Buzz"
        if (value %3 == 0) and (value%5 == 0):
            return "FizzBuzz"
        
        return str(value)