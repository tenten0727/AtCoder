import time

ans = 0

x = 2
y = 2
start = time.time()
for i in range(10**6):
    ans = x * y
end = time.time()

print(end - start)

# 10倍くらい遅い
x = 2**10000
y = 2
start = time.time()
for i in range(10**6):
    ans = x * y
end = time.time()

print(end - start)