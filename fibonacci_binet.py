# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 19:16:42 2021

This program calculates the nth fibonacci number using Binet formula.

@author: anders
"""

import time
import decimal

start = time.time()

n = 1000000

decimal.getcontext().prec = 300000

def fibonacci(n):
    square5 = decimal.Decimal(5).sqrt()
    phi = (1+square5)/2
    num = ((phi**n) - ((-phi)**(-n)))/square5
    return round(num)

fib = fibonacci(n)

print('The number has {num} digits, and can be viewed in fibonacci.text'.format(num=len(str(fib))))
print('It took {time} seconds to calculate.'.format(time=round(time.time()-start,5)))
file = open("fibonacci.txt","w+")
file.write('{n}th fibonacci numbers is: \n{num}'.format(n=n, num=fib))
file.close()

