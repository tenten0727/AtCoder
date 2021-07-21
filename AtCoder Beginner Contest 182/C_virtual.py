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
    s = s_input()
    count = Counter(s)
    a = count['1'] + count['4'] + count['7']
    b = count['2'] + count['5'] + count['8']
    
    n = int(s)
    c = n % 3
    if c == 0:
        print(0)
    elif c == 1:
        if a > 0 and len(s) > 1:
            print(1)
        elif b > 1 and len(s) > 2:
            print(2)
        else:
            print(-1)
    else:
        if b > 0 and len(s) > 1:
            print(1)
        elif a > 1 and len(s) > 2:
            print(2)
        else:
            print(-1)

if __name__ == '__main__':
    main()