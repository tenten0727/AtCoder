xy = list(map(int,input().split()))

ans = 'No'
if (xy[0] > xy[1] and xy[0] - xy[1] < 3) or (xy[1] > xy[0] and xy[1] - xy[0] < 3):
    ans = 'Yes'

print(ans)