X = str(input())
M = int(input())

# def Base_n_to_10(X,n):
#     out = 0
#     for i in range(1,len(str(X))+1):
#         out += int(X[-i])*(n**(i-1))
#     return out

def Base_10_to_n(X, n):
    if (int(X/n)):
        return Base_10_to_n(int(X/n), n)+str(X%n)
    return str(X%n)

d = max(list(map(int, list(X))))

ans = 0
n = d+1
while True:
    tmp = int(Base_10_to_n(int(X), n))
    if tmp <= M:
        ans += 1
        n += 1
    else:
        break

print(ans)

#2分探索！！！