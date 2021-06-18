import math
d, g = map(int, input().split())
g = g // 100
P = []
C = []

for _ in range(d):
    p, c = map(int, input().split())
    c = c // 100
    P.append(p)
    C.append(c)

ans = float("inf")

def dfs(i, score, num, nokori):
    global ans
    if i == d:
        if score >= g:
            ans = min(ans, num)
        else:
            if len(nokori) != 0:
                m = max(nokori)
                n = min(P[m-1], math.ceil((g - score) / m))
                if(score + n * m >= g):
                    ans = min(ans, num+n)
    else:
        dfs(i+1, score+(i+1)*P[i]+C[i], num+P[i], nokori)
        dfs(i+1, score, num, nokori+[i+1])

dfs(0, 0, 0, [])

print(int(ans))
