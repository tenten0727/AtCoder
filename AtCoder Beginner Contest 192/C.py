N, K = map(int, input().split())

def f(x):
    g1 = int(''.join(sorted(x, reverse=True)))
    g2 = int(''.join(sorted(x)))
    return g1 - g2
    

x = str(N)
for i in range(K):
    x = str(x)
    x = f(x)

print(x)