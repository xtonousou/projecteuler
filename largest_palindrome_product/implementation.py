#!/usr/bin/env python2
 
def find_max_palindrome(min = 100, max = 999):
  max_palindrome = 0
  a = 999
  while a > 99:
    b = 999
    while b >= a:
      prod = a * b
      if prod > max_palindrome and str(prod) == (str(prod)[::-1]):
        max_palindrome = prod
      b -= 1
    a -= 1
  return max_palindrome
 
print find_max_palindrome()
