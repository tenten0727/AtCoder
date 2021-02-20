import numpy as np
N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

A = np.array(A)
B = np.array(B)

ans = 'No'
if np.dot(A, B) == 0:
    ans = 'Yes'

print(ans)