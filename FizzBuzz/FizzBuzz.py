import sys
from FizzBuzzClass import *

def GetRange(argv):
    if len(sys.argv) != 3:
        return 1, 100
    else:
        return int(sys.argv[1]), int(sys.argv[2])


fizzBuzzCheck = FizzBuzz()

first, last = GetRange(sys.argv)

for num in range(first,last+1):
    isFizz = fizzBuzzCheck.CheckFizz(num)
    isBuzz = fizzBuzzCheck.CheckBuzz(num)
    fizzBuzzCheck.PrintFizzBuzz(num, isFizz, isBuzz)

    # fizzBuzzCheck.PrintFizzBuzz(num, fizzBuzzCheck.CheckFizz(num), fizzBuzzCheck.CheckBuzz(num))