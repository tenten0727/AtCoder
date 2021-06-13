a, b, c = map(int, input().split())

ans = '='
if a == b or (abs(a) == abs(b) and c % 2 == 0):
    print(ans)
    exit()

if a >= 0 and b >= 0:
    if a > b:
        ans = '>'
    else:
        ans = '<'
elif a < 0 and b >= 0:
    if c % 2 == 0:
        if abs(a) > abs(b):
            ans = '>'
        else:
            ans = '<'
    else:
        ans = '<'
elif a >= 0 and b < 0:
    if c % 2 == 0:
        if abs(a) > abs(b):
            ans = '>'
        else:
            ans = '<'
    else:
        ans = '>'
else:
    if c % 2 == 0:
        if abs(a) > abs(b):
            ans = '>'
        else:
            ans = '<'
    else:
        if abs(a) > abs(b):
            ans = '<'
        else:
            ans = '>'

print(ans)