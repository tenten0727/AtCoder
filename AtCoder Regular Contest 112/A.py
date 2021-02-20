T = int(input())
case = list(list(map(int, input().split())) for _ in range(T))
ans = 0

for c in case:
    L, R = c[0], c[1]
    if 2*L > R:
        ans = 0
    else:
        ans = int((R-2*L+1) * (R-2*L+2) / 2)
    print(ans)
