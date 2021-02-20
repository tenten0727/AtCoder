import numpy as np
N = int(input())
A = list(map(int,input().split()))
A1 = A[:int((2**N)/2)]
A2 = A[int((2**N)/2):]

A1np = np.array(A1)
A2np = np.array(A2)

max1 = np.argmax(A1np)
max2 = np.argmax(A2np)

if A1np[max1] < A2np[max2]:
    ans = max1+1
else:
    ans = max2+1+int((2**N)/2)

print(ans)