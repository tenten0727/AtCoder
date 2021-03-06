N = int(input())
A = list(map(int, input().split()))

b = 0
c = 0
for a in A:
    b += a*a
    c += a
print(b*N - c*c)

# python3で実行したらAC