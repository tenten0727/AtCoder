N = int(input())
B = list(map(int, input().split()))

ans = B[0]
if N >= 3:
    for i in range(0, N-2):
        ans += min(B[i], B[i+1])

    ans += B[-1]
elif N == 2:
    ans += B[0]

print(ans)