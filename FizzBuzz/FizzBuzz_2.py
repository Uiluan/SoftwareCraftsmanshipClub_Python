import sys
import string
from FizzBuzzClass_2 import *

fizzBuzzCheck = FizzBuzz()

allowedInput = set(string.digits + " ")
validInputEntered = False

while (not validInputEntered):
    userRange = input("Enter range (two values, separated by a space): ")
    if set(userRange) <= allowedInput:
        userRange = userRange.split()
        userRange = [int(num) for num in userRange]
        if len(userRange) == 2:
            for num in range(userRange[0], userRange[1]+1):
                fizzBuzzCheck.PrintFizzBuzz(num, fizzBuzzCheck.CheckFizz(num), fizzBuzzCheck.CheckBuzz(num))
            validInputEntered = True

    if not validInputEntered:
        print("Invalid input. Please enter two values, separate by a space (e.g. 1 100)")