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
def s_row(N): return [s_input() for _ in range(N)]
def s_row_str(N): return [s_list() for _ in range(N)]
def s_row_list(N): return [list(s_input()) for _ in range(N)]
def lcm(a, b): return a * b // gcd(a, b)
sys.setrecursionlimit(10 ** 6)
INF = float('inf')
MOD = 10 ** 9 + 7

def main():
    n = i_input()
    XY = i_row_list(n)
    S = s_input()
    
    # 右を向いている人の中で一番左の人　と　左を向いている人の中で一番右の人を見れば十分
    point = {}
    for i, (x, y) in enumerate(XY):
        if y not in point:
            point[y] = {'R': x, 'L': -INF} if S[i] == 'R' else {'R': INF, 'L': x}
        else:
            if S[i] == 'R': point[y]['R'] = min(point[y]['R'], x)
            if S[i] == 'L': point[y]['L'] = max(point[y]['L'], x)
    
    Y = set([y for y, y in XY])

    for y in Y:
        if point[y]['L'] - point[y]['R'] > 0:
            print('Yes')
            return
    
    print('No')



if __name__ == '__main__':
    main()