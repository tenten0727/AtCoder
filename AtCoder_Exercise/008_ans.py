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

def main():
	n = i_input()
	S = s_input()
	atcoder = list('atcoder')

	dp = [[0] * 8 for _ in range(n+1)]
	dp[0][0] = 1
	for i, s in enumerate(S):
		for x in range(8):
			# i文字目を選ばなかった場合
			dp[i+1][x] += dp[i][x]
			dp[i+1][x] %= MOD

			# i文字目を選んだ場合
			if x != 7 and s == atcoder[x]:
				dp[i+1][x+1] += dp[i][x]
				dp[i+1][x+1] %= MOD
	
	# for i in range(n+1):
	# 	print(dp[i])
	print(dp[-1][-1])


if __name__ == '__main__':
	main()
