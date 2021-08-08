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

ans = []
seen = []
def dfs(i, graph):
    global ans
    global seen
    seen[i] = True
    ans.append(str(i+1))
    for j in graph[i]:
        if seen[j]: continue
        dfs(j, graph)
        ans.append(str(i+1))
    
def main():
    n = i_input()
    graph = [[] for _ in range(n)]
    for i in range(n-1):
        a, b = i_map()
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)
    for i in range(n):
        graph[i].sort()

    global seen
    seen = [False for _ in range(n)]
    seen[0] = True

    global ans
    for i in graph[0]:
        ans.append(str(1))
        dfs(i, graph)
    ans.append(str(1))

    print(' '.join(ans))

if __name__ == '__main__':
    main()