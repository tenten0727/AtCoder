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

def bfs(r, c, sx, sy, gx, gy, maze):
    d = [[float("inf")] * c for i in range(r)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    
    que = deque([])
    que.append((sx, sy))
    d[sy][sx] = 0
    
    while que:
        p = que.popleft()
        if p[0] == gx and p[1] == gy:
            break
        for i in range(4):
            nx = p[0] +dx[i]
            ny = p[1] +dy[i]
            
            if 0 <= nx < c and 0 <= ny < r and maze[ny][nx] != '#' and d[ny][nx] == float("inf"):
                que.append((nx, ny))
                d[ny][nx] = d[p[1]][p[0]] + 1
    
    return d[gy][gx]
    
def main():
    r, c = i_map()
    sy, sx = i_map()
    gy, gx = i_map()
    sx -= 1
    sy -= 1
    gx -= 1
    gy -= 1
    maze = [list(input()) for i in range(r)]

    print(bfs(r, c, sx, sy, gx, gy, maze))

    
if __name__ == '__main__':
    main()