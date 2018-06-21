"""
Lattice paths
Problem 15
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.


How many such routes are there through a 20×20 grid?
"""

import math
a=1
for i in reversed(range(21,41)):
    a*=int(i)
print(int(a/math.factorial(20)))
