import collections

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))


D = [B[i-1] for i in C]
Dcount = collections.Counter(D)

ans = 0

for a in A:
    ans += Dcount[a]

print(ans)