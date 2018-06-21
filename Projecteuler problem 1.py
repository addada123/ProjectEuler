"""
Multiples of 3 and 5
Problem 1
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""
import time
start = time.time()
i = 0
a = 0
while (i<999):
    i += 1
    if (i % 3 == 0 or i % 5 == 0):
        a = a + i
print(a)
elapsed = time.time() - start
print("Time: {:.5f} seconds".format(elapsed))



