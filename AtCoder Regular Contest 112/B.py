B, C = map(int, input().split())

ans = 1

if B == 0:
    ans += C//2
    ans += (C-1)//2
elif B > 0:
    ans += min(B, C//2)*2 # 間
    if C//2 >= B*2:
        ans += 1
    ans += (C-1)//2 if C != 1 and C != 2 else 1 #マイナス側
    ans += (C-2)//2 if C != 1 else 0 #プラス側
else:
    ans += min(-2*B, (C-1)//2) # 間
    ans += C//2  #マイナス側
    ans += (C-1)//2 if C != 1 else 1 #プラス側

print(ans)
