"""
Problem 4

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
import time
start = time.time()
list3 = list()
for i in range(2,1000):
    for num in range(2,1000):
        num = i*num
        ters = int(str(num)[::-1])
        if num == ters:
            list3.append(num)
            list3.sort(reverse=True)
print(list3[0])
elapsed = time.time() - start
print("Time: {:.5f} seconds".format(elapsed))