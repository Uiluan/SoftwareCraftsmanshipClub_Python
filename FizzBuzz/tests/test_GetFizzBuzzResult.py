from FizzBuzzChecker import *


def test_Fizz():
    checker = FizzBuzzChecker()

    for value in range(1, 101):
        if (value % 3 == 0) and (not value % 5 == 0):
            result = checker.GetFizzBuzzResult(value)
            assert result == "Fizz", f"Expected Fizz, got: {result}"

def test_Buzz():
    checker = FizzBuzzChecker()

    for value in range(1, 101):
        if (value % 5 == 0) and (not value % 3 == 0):
            result = checker.GetFizzBuzzResult(value)
            assert result == "Buzz", f"Expected Buzz, got: {result}"

def test_FizzBuzz():
    checker = FizzBuzzChecker()

    for value in range(1, 101):
        if (value % 5 == 0) and (value % 3 == 0):
            result = checker.GetFizzBuzzResult(value)
            assert result == "FizzBuzz", f"Expected FizzBuzz, got: {result}"

def test_NotFizzOrBuzz():
    checker = FizzBuzzChecker()

    for value in range(1, 101):
        if (not value % 5 == 0) or (not value % 3 == 0):
            result = checker.GetFizzBuzzResult(value)
            assert result == str(value), f"Expected {value}, got: {result}"