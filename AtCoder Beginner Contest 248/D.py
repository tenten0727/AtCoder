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

# 境界線を意識（search以上の値の最初のインデックスがr）
def binary_search_left(L, search):
    l = -1
    r = len(L)

    while r - l > 1:
        mid = (r + l) // 2
        if L[mid] >= search:
            r = mid
        else:
            l = mid
    return r

def binary_search_right(L, search):
    l = -1
    r = len(L)

    while r - l > 1:
        mid = (r + l) // 2
        if L[mid] > search:
            r = mid
        else:
            l = mid
    return r

def main():
    n = i_input()
    A = i_list()
    q = i_input()
    Q = i_row_list(q)

    indexes = {i:[] for i in range(n+1)}

    for i, a in enumerate(A):
        indexes[a].append(i+1)
    
    for i in range(q):
        l, r, x = Q[i]
        st = binary_search_left(indexes[x], l) # l以上の値となる最初のindex(同じ値の場合は左の位置)
        gl = binary_search_right(indexes[x], r) # rより大きい値となる最初のindex(同じ値の場合は右の位置)
        print(gl - st)
        # print(bisect_right(indexes[x], r) - bisect_left(indexes[x], l))

if __name__ == '__main__':
    main()

'''
A = [3 1 4 1 5]
2 4 3 の時
indexes[3] = [0]
st = 1, gt = 1

indexだから1引いた値で計算しなければ。
'''