n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
 
c = 0
amax = 0
for k in range(n):
    amax = max(amax, a[k])
    c = max(c, amax*b[k])
    print(c)


# 高速化を意識！！
# リストにいちいちappendしていたのが時間オーバーの原因だと思われる