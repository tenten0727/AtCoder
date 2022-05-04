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

def permutations_count(n, r):
    return factorial(n) // factorial(n - r)

def main():
    N, M, K = i_map()

    l = [[0] * (K+1) for _ in range(N+1)] # 二次元配列の初期化方法　イミュータブルかミュータブルかの意識
    # 整数はイミュータブルのため値が変更されるとアドレスも変更
    # リストはミュータブルのため値が変更してもアドレスは変わらない
    # リストの*は参照渡し
    l[0][0] = 1
    
    for n in range(N):
        for k in range(K):
            for m in range(1, M+1):
                if k+m <= K:
                    l[n+1][k+m] += l[n][k] % 998244353

    ans = 0

    for k in range(K+1):
        ans += l[N][k] % 998244353
    
    ans %= 998244353
    print(ans)

if __name__ == '__main__':
    main()