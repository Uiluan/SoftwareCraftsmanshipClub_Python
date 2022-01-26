FIZZVALUE = 3
BUZZVALUE = 5

class FizzBuzz():
    #define Determine Fizz/Buzz for a single number
    def __init__(self) -> None:
        pass

    def CheckFizz(self, value):
        if value % FIZZVALUE == 0 and str(FIZZVALUE) in str(value):
            return True
        else:
            return False

    def CheckBuzz(self, value):
        if value % BUZZVALUE == 0 and str(BUZZVALUE) in str(value):
            return True
        else:
            return False

    def PrintFizzBuzz(self, value, isFizz, isBuzz):
        result = ""
        if isFizz:
            result = result + "Fizz"
        if isBuzz:
            result = result + "Buzz"
        if not isFizz and not isBuzz:
            result = value

        print(result)
