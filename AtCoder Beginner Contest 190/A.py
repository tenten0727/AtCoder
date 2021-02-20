A, B, C = list(map(int,input().split()))

ans = ""

if(C == 0):
    if(A > B):
        ans = "Takahashi"
    else:
        ans = "Aoki"
else:
    if(B > A):
        ans = "Aoki"
    else:
        ans = "Takahashi"

print(ans)