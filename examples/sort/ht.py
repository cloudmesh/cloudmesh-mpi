#!/usr/bin/env python
import random
import sys
import time
import numpy as np
from collections import Counter
from cloudmesh.common.StopWatch import StopWatch

from generate import Generator

n = 1000000

a = Generator().generate_random(n)
arraya = np.array(a)
b = np.random.randint(n, size=n)

counter_objectb = Counter(b)

print(len(a))
# print(a)
print(len(b))
# print(b)

StopWatch.start("sorted")
a = sorted(arraya)
StopWatch.stop("sorted")
# print(a)

StopWatch.start("list)")
l = b.tolist()
l1 = list(b)
StopWatch.stop("list)")

print(type(l))
print(type(l1))

StopWatch.start("np")
b = sorted(b)
StopWatch.stop("np")
# print(l)

StopWatch.benchmark()


