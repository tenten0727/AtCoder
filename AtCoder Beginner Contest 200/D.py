import collections
import math

def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

N = int(input())
A = map(int, input().split())
A = list(i % 200 for i in A)
ans = 0
c = collections.Counter(A)

for count in list( i for i in c.values() if i != 1):
    ans += combinations_count(count, 2)

print(ans)