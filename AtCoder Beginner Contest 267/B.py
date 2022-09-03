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
num_list = []
str_list = []

def main():
    S = s_input()
    
    rows = [[6], [3], [1, 7], [0, 4], [2, 8], [5], [9]]
    all_fall = [True for _ in range(len(rows))]

    if S[0] == '1':
        print('No')
        return
    
    for r, num in enumerate(rows):
        for i in num:
            if S[i] == '1':
                all_fall[r] = False
    
    state = 0
    for f in all_fall:
        if (state == 0) & ~f:
            state = 1
        if (state == 1) & f:
            state = 2
        if (state == 2) & ~f:
            print('Yes')
            return

    print('No')

if __name__ == '__main__':
    main()