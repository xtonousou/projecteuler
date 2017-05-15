#!/usr/bin/env python2

def fibonacci():
  a, b = 0, 1
  yield a
  yield b
  while True:
    a, b = b, a + b
    yield b

def sub_fibonacci(startNumber, endNumber):
  for number in fibonacci():
    if number > endNumber: return
    if number >= startNumber:
      yield number

sum = 0
for i in sub_fibonacci(2, 4000000):
  if (i % 2 == 0):
    sum += i

print sum
