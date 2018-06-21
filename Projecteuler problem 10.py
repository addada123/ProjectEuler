"""
Summation of primes
Problem 10
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
import time
start = time.time()
def prime(a):
    b = int((a ** 0.5) // 1) + 1
    if a == 1:
        return False
    elif a == 2:
        return True
    for i in range(2,b):
        if (a%i==0):
            return False
    return True
a = 2
sum = 0
while a<=2000000:
    b = int((a**0.5)//1)+1
    if prime(a):
       sum+=a
    a+=1
print(sum)
elapsed = time.time() - start
print("Time: {:.5f} seconds".format(elapsed))