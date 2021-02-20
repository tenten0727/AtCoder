a, b, x, y = map(int, input().split())
ans = 0
if y < 2*x:
    k = y
else:
    k = 2*x

if a > b:
    ans = x + k*(a-b-1)
elif a == b:
    ans = x
else:
    ans = x + k*(b - a)

print(ans)