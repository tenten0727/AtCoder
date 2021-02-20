N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = min(A[0]+A[1], B[0])

ai = A[0]

for i in range(1, N):
    ai = max(A[i] - max(B[i-1] - ai, 0), 0)
    ans += min(ai+A[i+1], B[i])


print(ans)