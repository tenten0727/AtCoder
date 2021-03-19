N, M, Q = map(int, input().split())
WV = list(list(map(int, input().split())) for _ in range(N))
X = list(map(int, input().split()))
LR = list(list(map(int, input().split())) for _ in range(Q))

WV = sorted(WV, key=lambda WV:WV[1], reverse=True) # sort by value

for l, r in LR:
    ans = 0
    box = list(x for i, x in enumerate(X) if i+1 < l or i+1 > r)
    box.sort()
    for w, v in WV:
        for i, b in enumerate(box):
            if b >= w:
                ans += v
                box.pop(i)
                break
    print(ans)

