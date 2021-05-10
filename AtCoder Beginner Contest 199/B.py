N = int(input())
A = map(int, input().split())
B = map(int, input().split())

a = max(A)
b = min(B)

ans = b-a+1
if ans < 0:
	print(0)
else:
	print(ans)
