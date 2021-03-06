X = str(input())
M = int(input())

def Base_n_to_10(X,n):
    out = 0
    for i in range(1,len(str(X))+1):
        out += int(X[-i])*(n**(i-1))
    return out

# def Base_10_to_n(X, n):
#     if (int(X/n)):
#         return Base_10_to_n(int(X/n), n)+str(X%n)
#     return str(X%n)

d = max(list(map(int, list(X))))

ans = 0
n = d+1


if int(X) < 10:
    if int(X) > M:
        ans = 0
    else:
        ans = 1
else:
    ok = d
    ng = M+1
    while ng - ok > 1:
        n = (ok + ng) // 2
        tmp = Base_n_to_10(X, n)
        if tmp <= M:
            ok = n
        elif tmp > M:
            ng = n
    
    ans = ok - d
print(ans)

#2分探索！！！