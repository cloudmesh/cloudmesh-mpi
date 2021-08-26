import random as r
import math as m
import time

start = time.time()

inside = 0                        # Number of darts that land inside.
trials = 100000                   # Number of Trials.

for i in range(0, trials):        # Iterate for the number of darts.
    x2 = r.random()**2            # Generate random x, y in [0, 1]
    y2 = r.random()**2

    if m.sqrt(x2 + y2) < 1.0:     # Increment if inside unit circle.
        inside += 1

# inside / trials = pi / 4
pi = (float(inside) / trials) * 4
end = time.time()

print(pi)                          # Value of pi found
print(end - start)                 # Execution time
