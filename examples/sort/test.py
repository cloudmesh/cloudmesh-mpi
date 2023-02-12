#!/usr/bin/env python
from sequential.mergesort import mergesort
from util.generate import Generator

a = Generator.generate_random(50)
a = sorted(a)
b = Generator.generate_random(50)
b = sorted(b)
print(a + b)
arr = mergesort('<', a + b)
print(arr)