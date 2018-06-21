"""
Problem 7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""
import time
start = time.time()
def prime(a):
    b = int((a ** 0.5) // 1) + 1
    if a == 1:
        return False
    elif a == 2:
        return True
    for i in range(2,b+1):
        if (a%i==0):
            return False
    return True
answer = list()
a = 2
while True:
    b = int((a**0.5)//1)+1
    if prime(a):
        answer.append(a)
    if len(answer)==10001:
        answer.sort(reverse=True)
        break
    a+=1
print(answer[0])
elapsed = time.time()-start
print("Time {:.5f} seconds".format(elapsed))
