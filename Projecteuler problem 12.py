"""
Highly divisible triangular number
Problem 12
The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
"""

import time
start = time.time()
def triangle(a):
    tri = int((a*(a+1))/2)
    return tri

def divisor(x):
    wq = 1
    e = int((x*0.5)//1)+1
    for i in range(1,e):
        if x % i == 0:
            wq+=1
    return wq

a = 1
while True:
    if triangle(a)%2==0 and triangle(a)%3==0 and triangle(a)%5==0 and triangle(a)%7==0 and triangle(a)%13==0 and triangle(a)%17==0:
        x = triangle(a)
        if divisor(x)>=500:
            print(divisor(x))
            print(x)
            elapsed = time.time()-start
            print("Time: {:.5f} seconds".format(elapsed))
            break
    a+=1