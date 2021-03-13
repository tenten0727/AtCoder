N = int(input())

ans = 0
A = 0
i = 0
while (N - A) > 0:
    A += 999*(1000**i)
    ans += N - A
    i += 1
ans -= N - A
print(ans)