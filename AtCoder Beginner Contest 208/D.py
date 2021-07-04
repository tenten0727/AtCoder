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
    n, m = i_map()

    graph = [[0]*n for _ in range(n)]
    for _ in range(m):
        u, v, w = i_map()
        graph[u-1][v-1] = w
    ans = 0
    
    for s in range(n):
        for t in range(n):
            for k in range(n):
                if s == t:
                    break
                used = [False for _ in range(n)]
                dist = [INF for _ in range(n)]
                dist[s] = 0
                X = set(range(k))
                X.add(s)
                X.add(t)
                for i in X:
                    min_dist = INF
                    min_v = -1

                    for j in X:
                        if not used[j] and dist[j] < min_dist:
                            min_dist = dist[j]
                            min_v = j
                    
                    if min_v == -1:
                        break
                    
                    for v, w in enumerate(graph[min_v]):
                        dist[v] = min(dist[v], dist[min_v]+w)
                    
                    used[min_v] = True
                
                if dist[t] != INF:
                    print(dist[t])
                    ans += dist[t]
    
    print(ans)


if __name__ == '__main__':
    main()