#!/usr/bin/env python2


def IsPrime(num):
    for i in range(2, num):
        if (num % i) == 0:
            return False
    return True


def FindThatDamnPrime():
    current = 2
    count = 0
    while True:
        if count == 10001:
            break
        if IsPrime(current):
            count += 1
        current += 1
    return current - 1


print FindThatDamnPrime()
