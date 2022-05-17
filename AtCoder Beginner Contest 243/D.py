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
    n, x = i_map()
    S = s_input()

    cnt = Counter(S)

    # if cnt['U'] >= cnt['R'] + cnt['L']:
    #     for c in range(cnt['U'] - (cnt['R'] + cnt['L'])):
    #         x = x // 2
    # else:
    new_S = ''
    delete = 0
    for i in range(1, n+1):
        s = S[-i]
        if s == 'U':
            delete += 1
        else:
            if delete > 0:
                delete -= 1
            else:
                new_S += s
    
    if delete > 0:
        for i in range(delete):
            x = x // 2
    for new_s in new_S[::-1]:
        x = 2 * x if new_s == 'L' else 2 * x + 1

    print(x)

    # TLE 桁数の多い計算を何回も行うため
    # for s in S:
    #     if s == 'U':
    #         x = x // 2
    #     elif s == 'L':
    #         x = 2 * x
    #     else:
    #         x = 2 * x + 1
    
    # print(x)

if __name__ == '__main__':
    main()