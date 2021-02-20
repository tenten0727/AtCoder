ab = []

N, M, T = map(int, input().split())

ans = N
out = 'Yes'
for i in range(M):
    ab.append(list(map(int, input().split())))

for i in range(M):
    if i == 0:
        ans -= ab[i][0]
    else:
        ans -= ab[i][0] - ab[i-1][1]
    if ans <= 0:
        out = 'No'
        break
    ans += ab[i][1] - ab[i][0]
    if ans > N:
        ans = N

ans -= T - ab[M - 1][1]
if ans <= 0:
    out = 'No'

print(out)