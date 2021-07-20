import sys, re
from math import ceil, floor, sqrt, pi, factorial, gcd
from copy import deepcopy
from collections import Counter, deque
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement
from bisect import bisect, bisect_left, bisect_right
from functools import reduce
from decimal import Decimal, getcontext
from typing import AsyncContextManager
def i_input(): return int(input())
def i_map(): return map(int, input().split())
def i_list(): return list(i_map())
def i_row(N): return [i_input() for _ in range(N)]
def i_row_list(N): return [i_list() for _ in range(N)]
def s_input(): return input()
def s_map(): return input().split()
def s_list(): return list(s_map())
def s_row(N): return [s_input for _ in range(N)]
def s_row_str(N): return [s_list() for _ in range(N)]
def s_row_list(N): return [list(s_input()) for _ in range(N)]
def lcm(a, b): return a * b // gcd(a, b)
sys.setrecursionlimit(10 ** 6)
INF = float('inf')
MOD = 10 ** 9 + 7
num_list = []
str_list = []

def main():
    # 累積和
    print(list(accumulate([1, 2, 4, 5, 6, 0])))
    
    # 二次元累積和
    n = 5
    A = [[1 for _ in range(n)] for _ in range(n)]
    A_sum = [[0 for _ in range(n+1)] for _ in range(n+1)]

    #方法１
    for i in range(n):
        for j in range(n):
            A_sum[i+1][j+1] = A[i][j] + A_sum[i+1][j] + A_sum[i][j+1] - A_sum[i][j]
    
    print('[')
    for r in A_sum:
        print(r)
    print(']')

    #方法２
    for i in range(n):
        for j in range(n):
            if j != 0:
                A[i][j] += A[i][j-1]
    for i in range(n):
        for j in range(n):
            if i != 0:
                A[i][j] += A[i-1][j]
    
    print('[')
    for r in A:
        print(r)
    print(']')
    

if __name__ == '__main__':
    main()