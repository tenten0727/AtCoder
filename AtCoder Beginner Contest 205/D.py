n, q = map(int, input().split())
A = list(map(int, input().split()))
K = list(int(input()) for _ in range(q))

def f(x, c):
    count = sum([i <= x for i in A])
    if count == c:
        return x
    return f(x+count-c, count)

for k in K:
    print(f(k, 0))