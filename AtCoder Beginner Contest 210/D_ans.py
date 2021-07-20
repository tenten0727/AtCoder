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

# 絶対値を外すことを考える（その際反転させればすべてのパターンを考えられることに注意）
# 場所ごとの計算に変換することができる
# dpを使って値を保存しておけば最小値がすぐに求められる
def main():
    h, w, c = i_map()
    A = i_row_list(h)
    
    ans = INF
    for _ in range(2):
        dp = [[INF] * w for _ in range(h)]
        for i in range(h):
            for j in range(w):
                dp[i][j] = A[i][j] - c * (i + j)
        
        for i in range(h):
            for j in range(w):
                if i != 0: dp[i][j] = min(dp[i][j], dp[i-1][j])
                if j != 0: dp[i][j] = min(dp[i][j], dp[i][j-1])
        
        for i in range(h):
            for j in range(w):
                tmp = INF
                if i != 0: tmp = min(tmp, dp[i-1][j])
                if j != 0: tmp = min(tmp, dp[i][j-1])
                ans = min(ans, A[i][j] + c * (i + j) + tmp)
                
        A = [list(reversed(a)) for a in A]

    print(ans)

if __name__ == '__main__':
    main()