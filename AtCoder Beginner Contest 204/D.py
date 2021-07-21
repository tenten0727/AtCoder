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

# 全探索だとTLE　→　動的計画法

# def dfs(n, T, t1, t2):
# 	global ans
# 	if n == 0:
# 		ans = min(ans, max(t1, t2))
# 	else:
# 		dfs(n-1, T, t1+T[n-1], t2)
# 		dfs(n-1, T, t1, t2+T[n-1])

# def main():
# 	n = i_input()
# 	T = i_list()
	
# 	dfs(n, T, 0, 0)

# 	print(ans)

def main():
	n = i_input()
	T = i_list()
	tot = sum(T)
	dp = [[INF] * (tot*2+1) for _ in range(n+1)]
	dp[0][0] = 0
	for i in range(n):
		for t in range(tot):
			if (dp[i][t] != INF):
				dp[i+1][t+T[i]] = min(dp[i+1][t+T[i]], dp[i][t])
				dp[i+1][t] = min(dp[i+1][t], dp[i][t]+T[i])

	ans = INF
	for t in range(tot):
		ans = min(ans, max(t, dp[n][t]))
	print(ans)

if __name__ == '__main__':
	main()
