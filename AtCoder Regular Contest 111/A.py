nm = list(map(float,input().split()))

ans = (int)((int)(10**nm[0]/nm[1]) % nm[1])

print(ans)