#!/usr/bin/env python2

def PythagoreanTriplet():
    for numAlpha in range(1, 1000):
        for numBeta in range(numAlpha, 1000 - numAlpha):
            numCharlie = 1000 - numAlpha - numBeta
            if numAlpha ** 2 + numBeta ** 2 == numCharlie ** 2:
                return numAlpha, numBeta, numCharlie, numAlpha * numBeta * numCharlie


print PythagoreanTriplet()
