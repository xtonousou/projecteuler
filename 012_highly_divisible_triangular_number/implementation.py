#!/usr/bin/env python2


def Factors(n):
    return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))


def FindThatNumber(n):
    currentNumber = n
    while True:
        triangularNumber = (currentNumber * (currentNumber + 1)) / 2
        if len(Factors(triangularNumber)) > 500:
            print triangularNumber
            break
        currentNumber += 1

FindThatNumber(1)
