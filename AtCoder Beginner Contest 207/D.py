import sys, re
from math import atan, ceil, cos, floor, sin, sqrt, pi, factorial, gcd, atan2
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

def mean(A):
    return sum(A) / len(A)

def main():
    n = i_input()
    AB = i_row_list(n)
    A = [a for a, b in AB]
    B = [b for a, b in AB]
    CD = i_row_list(n)
    C = [c for c, d in CD]
    D = [d for c, d in CD]
    
    if n == 1:
        print('Yes')
    else:
        A = [a - mean(A) for a in A]
        B = [a - mean(B) for a in B]
        CD = [[a - mean(C), b - mean(D)] for a, b in CD]
        C = [a - mean(C) for a in C]
        D = [a - mean(D) for a in D]
        
        for x, y in zip(A, B):
            if x != 0 or y != 0:
                break
        # print(x, y)
        for i in range(n):
            xi, yi = C[i], D[i]
            angle = atan2(yi, xi) - atan2(y, x)
            
            for j in range(n):
                xj = A[j]*cos(angle)-B[j]*sin(angle)
                yj = A[j]*sin(angle)+B[j]*cos(angle)
                flag = False
                for k in range(n):
                    if abs(xj - CD[k][0]) <= 1e-5 and abs(yj - CD[k][1]) <= 1e-5:
                        flag = True
                        break
                if not flag:
                    break
            if flag:
                print('Yes')
                exit()
        
        print('No')

if __name__ == '__main__':
    main()