#!/usr/bin/env python2

from math import sqrt
from itertools import count, islice


def IsPrime(n):
    return n > 1 and all(n % i for i in islice(count(2), int(sqrt(n) - 1)))


def FindSumOfPrimesUnder(limit):
    s = 0
    for num in xrange(3, limit):
        if IsPrime(num):
            s += num
    return s

print FindSumOfPrimesUnder(2000000)
