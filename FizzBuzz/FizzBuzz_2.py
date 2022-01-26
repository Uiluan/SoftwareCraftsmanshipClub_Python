import sys
from FizzBuzzClass_2 import *

def GetRange(argv): #TODO: Change to prompt for input instead
    if len(sys.argv) != 3:
        return 1, 100
    else:
        return int(sys.argv[1]), int(sys.argv[2])


fizzBuzzCheck = FizzBuzz()

first, last = GetRange(sys.argv)

for num in range(first,last+1):
    fizzBuzzCheck.PrintFizzBuzz(num, fizzBuzzCheck.CheckFizz(num), fizzBuzzCheck.CheckBuzz(num))