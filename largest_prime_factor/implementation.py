#!/usr/bin/env python2

def largest_prime_factor(number):
  i = 2
  while i * i <= number:
    if number % i:
      i += 1
    else:
      number //= i
  return number

print largest_prime_factor(600851475143)
