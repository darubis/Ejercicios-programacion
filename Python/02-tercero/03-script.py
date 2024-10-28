#!/usr/bin/env python3

import time
import sys

sys.setrecursionlimit(2000)

def factorial(n):
    answer = 1
    for i in range(2, n+1):
        answer *= i
    return answer

def factorial_r(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 1:
        return 1
    result = n * factorial_r(n - 1, memo)
    memo[n] = result
    return result

if __name__ == '__main__':
    n = 1000

    start = time.time()
    factorial(n)
    end = time.time()
    print("Factorial iterativo:", end - start)

    start = time.time()
    factorial_r(n)
    end = time.time()
    print("Factorial recursivo:", end - start)