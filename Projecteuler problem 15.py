"""
Lattice paths
Problem 15
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.


How many such routes are there through a 20×20 grid?
"""
#Just use simple math. Calculating grids routes like pascal triangle. 
#We can calculate it with how many square goes to bottom and left corner. 
#So in 2x2 grid it will be 4!/2!.2!=6 and in 3x3 grid => 6!/3!.3!=20
#20x20 grid => 40!/20!.20!=...
import math
a=1
for i in reversed(range(21,41)):
    a*=int(i)
print(int(a/math.factorial(20)))
