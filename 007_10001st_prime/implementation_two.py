#!/usr/bin/env python2


def IsPrime(num):
    if num % 2 == 0: return False
    p = 3
    while p < num ** 0.5 + 1:
        if num % p == 0: return False
        p += 2
    return True


def FindThatDamnPrime(num):
    current = 2
    count = 1
    step = 3
    while count < num:
        if IsPrime(step):
            current = step
            count += 1
        step += 2
    return current


print FindThatDamnPrime(10001)
