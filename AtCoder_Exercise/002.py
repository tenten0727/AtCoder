import sys, re
from math import ceil, floor, sqrt, pi, factorial, gcd
from copy import deepcopy
from collections import Counter, deque
from heapq import heapify, heappop, heappush
from itertools import accumulate, permutations, product, combinations, combinations_with_replacement, permutations
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
    ans = []
    if n % 2 == 0:   
        for c in combinations(range(n - 2), (n - 2) // 2):
            s = '('
            for k in range(n-2):
                if k in c:
                    s += '('
                else:
                    s += ')'
            s += ')'
            
            num = 0
            append = True
            for i in list(s):
                if i == '(':
                    num += 1
                else:
                    num -= 1
                
                if num < 0:
                    append = False

            if append:
                ans.append(s)
            
        ans.sort()

    for a in ans:
        print(a)

if __name__ == '__main__':
    main()