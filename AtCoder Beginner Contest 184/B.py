NX = list(map(int, input().split()))
S = input()

N = NX[0]
X = NX[1]

ans = X

for i in range(N):
    if S[i] == 'o':
        ans += 1
    else:
        if ans != 0:
            ans -= 1

print(ans)