import sys, re
from math import ceil, floor, log2, sqrt, pi, factorial, gcd
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

def calc(A, i, n):
    bit = 1
    tmp_list = [A[0]]
    ans = 0
    for j in range(1, n):
        tmp_ans = 0
        #分けるとき
        if bit & i:
            for a in tmp_list:
                tmp_ans |= a
            tmp_list=[]
        

        if ans != 0:
            ans ^= tmp_ans
        else:
            ans = tmp_ans
        
        bit = bit << 1
        tmp_list.append(A[j])
    tmp_ans = 0
    for a in tmp_list:
        tmp_ans |= a
    
    if ans != 0:
        ans ^= tmp_ans
    else:
        ans = tmp_ans
        
    return ans

def main():
    n = i_input()
    A = i_list()
    
    result = INF
    
    if n == 1:
        print(A[0])
        exit()
    
    for i in range(2**(n-1)):
        result = min(calc(A, i, n), result)
        # print(calc(A, i, n))

    print(result)

if __name__ == '__main__':
    main()