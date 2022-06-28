from array import array
from math import sqrt

def FindKPrimes(k: int, start: int, end: int) -> array:
    factors = []
    kprimes = []

    for num in range(start, end + 1):
        factors = factors + GetPrimeFactors(num)
        if len(DeterminePrimeFactorList(num, factors)) == k:
            kprimes.append(num)

    return kprimes

def GetPrimeFactors(value: int) -> array:
    factors = []

    for index in range(1, value):
        if value % index == 0 and IsPrime(index):
            factors.append(index)

    return factors

def DeterminePrimeFactorList(n: int, primeFactors: array) -> array:
    quotient = n
    primeFactorsTemp = primeFactors
    finalFactors = []

    while not IsPrime(quotient):
        if quotient % primeFactorsTemp[-1] == 0:
            quotient = quotient / primeFactorsTemp[-1]
            finalFactors.append(primeFactorsTemp[-1])
        else:
            primeFactorsTemp.pop()

    finalFactors.append(quotient)

    return finalFactors

def IsPrime(n: int) -> bool:
    # Primality test using 6k+-1 optimization.
    if n <= 3:
        return n > 1
    if not n % 2 or not n % 3:
        return False
    i = 5
    stop = int(n**0.5)
    while i <= stop:
        if not n % i or not n % (i + 2):
            return False
        i += 6
    return True

