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
    h, w, n = i_map()
    A = []
    B = []
    for i in range(n):
        a, b = i_map()
        A.append(a)
        B.append(b)
    
    As = sorted(list(set(A)))
    Bs = sorted(list(set(B)))
    Aans = {}
    Bans = {}
    for i, a in enumerate(As):
        Aans[a] = i+1
    for i, b in enumerate(Bs):
        Bans[b] = i+1

    for a, b in zip(A, B):
        print(Aans[a], Bans[b])

if __name__ == '__main__':
    main()