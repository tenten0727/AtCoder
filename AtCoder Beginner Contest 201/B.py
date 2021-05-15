N = int(input())
ST = list(list(input().split()) for _ in range(N))

T = list([int(st[1]), str(st[0])] for st in ST)

T.sort()
print(T[-2][1])