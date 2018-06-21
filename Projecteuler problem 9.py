"""
Special Pythagorean triplet
Problem 9
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
import time
start = time.time()
answer = list()
def pythagorean(a,b):
    c = int((((a**2+b**2)**0.5)//1))
    if c**2 ==(a**2+b**2) and a+b+c==1000:
        answer.append((a*b*c))
        return True
    return False
a = 1
while True:
    for b in range(1,a):
        if pythagorean(a,b):
            print(answer)
            elapsed = time.time() - start
            print("Time: {:.5f} seconds".format(elapsed))
            exit(1)
    a+=1
