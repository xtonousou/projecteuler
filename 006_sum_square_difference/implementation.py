#!/usr/bin/env python2


def SumOfSquares():
    sos = 0
    for num in range(1, 101):
        sos += num ** 2
    return sos


def SquareOfSum():
    sos = 0
    for num in range(1, 101):
        sos += num
    return sos ** 2


def Difference():
    return SquareOfSum() - SumOfSquares() 


print Difference()
