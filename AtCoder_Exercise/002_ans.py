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

# bit全探索
# （）の判定
def main():
    n = i_input()
    candidate = []
    
    for i in range(2 ** n):
        s = ''
        for j in range(n):
            if i & (1 << j):
                s += '('
            else:
                s += ')'
        
        candidate.append(s)
    
    candidate.sort()
    for can in candidate:
        num = 0
        ans = True
        for i in can:
            if i == '(':
                num += 1
            else:
                num -= 1
            
            if num < 0:
                ans = False
        
        if num != 0:
            ans = False
        
        if ans:
            print(can)

if __name__ == '__main__':
    main()