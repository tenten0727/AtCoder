import sys, re
from math import atan2, ceil, cos, degrees, floor, radians, sin, sqrt, pi, factorial, gcd
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
    n = i_input()
    p0 = i_list()
    p2 = i_list()
    
    mid = [(p0[0] + p2[0]) / 2, (p0[1] + p2[1]) / 2]
    
    r = sqrt((p0[0] - mid[0]) ** 2 + (p0[1] - mid[1]) ** 2)
    
    rotate = atan2(p0[1] - mid[1], p0[0] - mid[0])
    
    rad = radians(360/n)
    ans = [r * cos(rad), r * sin(rad)]
    
    ans = [ans[0] * cos(rotate) - ans[1] * sin(rotate) + mid[0], ans[0] * sin(rotate) + ans[1] * cos(rotate) + mid[1]]

    print(*ans)

if __name__ == '__main__':
    main()