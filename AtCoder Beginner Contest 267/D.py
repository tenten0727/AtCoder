import sys, re
from math import ceil, floor, sqrt, pi, factorial, gcd
from copy import deepcopy
from collections import Counter, deque
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement
from bisect import bisect, bisect_left, bisect_right
from functools import reduce
from decimal import Decimal, getcontext
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


def main():
    # dp?
    n, m = i_map()
    A = i_list()
    
    #dp[Aのリストの先頭からx個の中から][m個選んだ時の] = 最大値
    dp = [[-INF] * (m+1) for _ in range(n+1)]
    for i in range(n+1):
        dp[i][0] = 0

    for i in range(1, n+1):
        for j in range(1, m+1):
            if i < j:
                break
            dp[i][j] = max(dp[i-1][j-1] + A[i-1]*j, dp[i-1][j])

    print(dp[n][m])

if __name__ == '__main__':
    main()