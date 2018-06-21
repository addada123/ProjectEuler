"""
Largest prime factor
Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
import time
start = time.time()
a = 600851475143
i = 2
while i<a:
    while a % i == 0:
        a = a / i
    i += 1
print(a)
elapsed = time.time() - start
print("Time: {:.5} seconds".format(elapsed))