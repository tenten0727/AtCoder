import math

N = int(input())

n = int(math.sqrt(N))
ans = N
tmp = set()

for a in range(2, n+1):
	b = 2
	while a ** b <= N and a not in tmp:
		ans -= 1
		if a**b <= n:
			tmp.add(a ** b)
		b += 1

print(ans)
