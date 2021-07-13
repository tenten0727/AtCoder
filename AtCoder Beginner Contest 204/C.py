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

count = 0

def dfs(a, graph, seen):
    global count
    seen[a] = True
    count += 1

    for i in graph[a]:
        if seen[i]:
            continue
        dfs(i, graph, seen)


def main():
    n, m = i_map()
    graph = [[] for _ in range(n)]
    for _ in range(m):
        a, b = i_map()
        graph[a-1].append(b)
    
    for a in range(n):
        seen = [False for _ in range(n)]
        dfs(a, graph, seen)

    print(count)

if __name__ == '__main__':
    main()