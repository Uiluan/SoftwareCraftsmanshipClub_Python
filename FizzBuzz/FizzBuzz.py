import sys
from FizzBuzzClass import *

def GetRange(argv): #TODO: prompt for user input instead
    if len(sys.argv) != 3:
        return 1, 100
    else:
        return int(sys.argv[1]), int(sys.argv[2])


fizzBuzzCheck = FizzBuzz()

first, last = GetRange(sys.argv)

for num in range(first,last+1):
    fizzBuzzCheck.PrintFizzBuzz(num, fizzBuzzCheck.CheckFizz(num), fizzBuzzCheck.CheckBuzz(num))