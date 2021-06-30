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
	s = list(s_input())
	q = i_input()
	tab = i_row_list(q)
	flag = False

	for i in range(q):
		if tab[i][0] == 1:
			if flag:
				a = n if tab[i][1] - 1 < n else -n
				b = n if tab[i][2] - 1 < n else -n
				s[tab[i][1] - 1 + a], s[tab[i][2] - 1 + b] = s[tab[i][2] - 1 + b], s[tab[i][1] - 1 + a]

			else:
				s[tab[i][1] - 1], s[tab[i][2] - 1] = s[tab[i][2] - 1], s[tab[i][1] - 1]
		else:
			flag = not flag

	if flag:
		s = s[n:] + s[:n]

	print("".join(s))

if __name__ == '__main__':
	main()