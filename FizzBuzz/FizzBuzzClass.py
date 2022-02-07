FIZZVALUE = 3
BUZZVALUE = 5

class FizzBuzz():
    #define Determine Fizz/Buzz for a single number
    def __init__(self) -> None:
        pass

    def CheckFizz(self, value):
        if value % FIZZVALUE == 0:
            return True
        else:
            return False

    def CheckBuzz(self, value):
        if value % BUZZVALUE == 0:
            return True
        else:
            return False

#TODO: Can I refactor this to not require boolean input? Perhaps FizzBuzz status stored locally, new object created each loop?
    def PrintFizzBuzz(self, value, isFizz, isBuzz):
        result = ""
        if isFizz:
            result = result + "Fizz"
        if isBuzz:
            result = result + "Buzz"
        if not isFizz and not isBuzz:
            result = value

        print(result)
