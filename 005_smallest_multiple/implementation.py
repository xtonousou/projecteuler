#!/usr/bin/env python2


def FindLcm(a, b):
    lcm = hcf = 0
    i = 1
    ger = a if a < b else b
    while i <= ger:
        if (a % i == 0) & (b % i == 0):
            hcf = i
        i += 1
    lcm = (a * b) / hcf
    return lcm


def FindMultiple():
    lcm = 1
    for i in range(2, 21):
        lcm = FindLcm(lcm, i)
    return lcm

print FindMultiple()
