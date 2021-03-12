N = int(input())
AB = [map(int, input().split()) for _ in range(N)]
A, B = [list(i) for i in zip(*AB)]

add = 2*10e5

for i in range(N):
    add = min(A[i] + B[i], add)

A.sort()
B.sort()

if add == A[0] + B[0]:
    s = max(A[0], B[1])    
    t = max(A[1], B[0])  
    ans = min(s, t)
    ans = min(add, ans)
    print(ans)
else:
    print(max(A[0], B[0]))