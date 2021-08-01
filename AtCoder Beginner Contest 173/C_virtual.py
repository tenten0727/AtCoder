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

#bit全探索
def main():
    h, w, k = i_map()
    C = s_row_list(h)
    
    ans = 0
    for i in range(2**h):
        for j in range(2**w):
            tmp = 0
            for x in range(h):
                if (i & (1 << x)):
                    for y in range(w):
                        if (j & (1 << y)) and C[x][y] == "#":
                            tmp += 1
            if tmp == k:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()