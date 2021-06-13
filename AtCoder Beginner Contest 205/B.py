n = int(input())
A = list(map(int, input().split()))

A.sort()

A_ans = list(x for x in range(1, n+1))

if A == A_ans:
    print('Yes')
else:
    print('No')