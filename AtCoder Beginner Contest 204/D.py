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

ans = INF
memo = []

# 全探索だとTLE　→　動的計画法

def dfs(n, T, t1, t2):
	global ans
	if n == 0:
		ans = min(ans, max(t1, t2))
	else:
		dfs(n-1, T, t1+T[n-1], t2)
		dfs(n-1, T, t1, t2+T[n-1])

def main():
	n = i_input()
	T = i_list()
	
	dfs(n, T, 0, 0)

	print(ans)

if __name__ == '__main__':
	main()
