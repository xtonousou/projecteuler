#!/usr/bin/env python2

size = 20
paths = 1

for i in xrange(0, size):
    paths *= (2 * size) - i
    paths /= i + 1

print "Found %s paths in the %sx%s grid" % (paths, size, size)
