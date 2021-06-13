N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

ans = 0
for j, c in enumerate(C):
    b = B[c-1]
    ans += A.count(b)
    
print(ans)