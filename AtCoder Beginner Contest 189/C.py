# import numpy as np

# N = int(input())
# A = list(map(int, input().split()))

# A = np.array(A)

# m = A.min()
# apple = m * N

# for i in range(N-1):
#     if A[0] < A[-1]:
#         A = np.delete(A, 0)
#     else:
#         A = np.delete(A, -1)

#     m = A.min()
#     if(apple < m*(N-i-1)):
#         apple = m*(N-i-1)

# print(apple)

N=int(input())
A=list(map(int,input().split()))
ans=0
for i in range(N):
    tmp=10**9
    cnt=0
    for j in range(i,N):
        tmp=min(tmp,A[j])
        cnt+=1
        ans=max(ans,cnt*tmp)
print(ans)