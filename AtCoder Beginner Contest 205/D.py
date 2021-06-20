# n, q = map(int, input().split())
# A = list(map(int, input().split()))
# K = list(int(input()) for _ in range(q))

# def f(x, c):
#     count = sum([i <= x for i in A])
#     if count == c:
#         return x
#     return f(x+count-c, count)

# for k in K:
#     print(f(k, 0))



n, q = map(int, input().split())
A = list(map(int, input().split()))
K = list(int(input()) for _ in range(q))

C = [a - i - 1 for i, a in enumerate(A)]
A.insert(0, 0)
C.insert(0, 0)

def binary_search():
    left = 0
    right = n #場外はないけど一応
    
    while right - left > 1:
        mid = (right + left) // 2
        if C[mid] >= k:
            right = mid
        else:
            left = mid
    return right


ans = 0
for k in K:
    if k > C[n]:
        ans = A[n] + (k - C[n])
    else:
        x = binary_search()
        ans = A[x] - 1 - (C[x] - k)
    print(ans)