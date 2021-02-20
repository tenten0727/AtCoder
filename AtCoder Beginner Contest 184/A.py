ab = list(map(int,input().split()))
cd = list(map(int, input().split()))

ans = ab[0]*cd[1] - ab[1]*cd[0]

print(ans)