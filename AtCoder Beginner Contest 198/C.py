import math

R, X, Y = map(int, input().split())

ans = 0

ans = math.ceil((X ** 2 + Y ** 2) ** 0.5 / R)
if (X ** 2 + Y ** 2) ** 0.5 < R:
	ans = 2

print(ans)
