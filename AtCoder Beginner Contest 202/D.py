import math

def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

A, B, K = map(int, input().split())

ans = ''
N = A + B
count = 0
a = A
b = B

for n in range(N, 0, -1):
    if a <= 0:
        for _ in range(b):
            ans = ans + 'b'
        break
    
    if b <= 0:
        for _ in range(a):
            ans = ans + 'a'
        break

    if count + combinations_count(a+b-1, b) >= K:
        ans = ans + 'a'
        a -= 1
    else:
        count += combinations_count(a+b-1, b)
        ans = ans + 'b'
        b -= 1
    
print(ans)