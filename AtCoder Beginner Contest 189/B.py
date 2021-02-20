from decimal import Decimal
N, X = list(map(int,input().split()))

alc = Decimal(0)
ans = -1

X = Decimal(X)

for i in range(N):
    VP = list(map(Decimal,input().split()))
    alc += VP[0] * (VP[1] / Decimal(100))
    if alc > X:
        ans = i+1
        break

print(ans)
