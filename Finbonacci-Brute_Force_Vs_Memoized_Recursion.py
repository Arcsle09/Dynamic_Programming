# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 07:08:15 2021

@author: chra8017

"""

#Find nth Fibonnaci Number

def fib_bruteforce(n):
    if n <=2:
        return 1
    return fib_bruteforce(n-1) + fib_bruteforce(n-2)


#The brute force method will work smoothly when the function has
#small input number.

#fib_bruteforce(5)
#fib_bruteforce(6)
#fib_bruteforce(7)

#The brute force method will take very long time when the function has
#big input number.
#fib_bruteforce(50)

# To Solve above problem, we will need to optimize the above solution by 
#using MEMOIZATION method. 

def fib_memoization(n,memo = {}):
    if n in memo:
        return memo[n]
    if n <=2:
        return 1
    memo[n] = fib_memoization(n-1,memo) + fib_memoization(n-2,memo)
    return memo[n]

#The function fib_memoization(35) will return the value blazingly fast in comparison to fib_bruteforce(35)

# %timeit fib_bruteforce(35) --> 2.86 s ± 352 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)   

# %timeit fib_memoization(35) --> 170 ns ± 2.74 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)
