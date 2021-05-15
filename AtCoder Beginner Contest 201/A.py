a, b, c = map(int, input().split())

if (c - b == b - a) or (a - c == c - b) or (c - a == a - b):
    print('Yes')
else:
    print('No')