N = int(input())

A = list(list(map(int, input().split())) for _ in range(N))

ans = -1
for a in A:
	if a[2] - a[0] > 0:
		ans = min(ans, a[1]) if ans != -1 else a[1]
	
print(ans)
