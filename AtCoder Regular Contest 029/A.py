import itertools

N = int(input())
T = [int(input()) for _ in range(N)]

ans = float('inf')
for i in range(N//2+1):
    for j in itertools.combinations(range(N), r=i):
        a = [T[x] for x in j]
        b = [T[x] for x in range(N) if x not in j]        
        ans = min(ans, max(sum(a), sum(b)))
        
print(ans)

