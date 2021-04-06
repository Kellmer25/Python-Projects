# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 19:01:03 2021

A program that caluculates the n'th fibonacci number using recursion.

Note that this method is rather inefficient.
For reference the 35th number takes approx 4.82 seconds and
the 40th takes 51.53 seconds on my hardware.

@author: ander
"""

import time

start = time.time()

n = 40

def fibonacci(n):
    if n <= 1:
        return n
    else: 
        return fibonacci(n-1) + fibonacci(n-2)

print('The {n}th fibonacci number is {num}.'.format(n=n, num=fibonacci(n)))
print('It took {time} seconds to calculate'.format(time=round(time.time()-start,5)))