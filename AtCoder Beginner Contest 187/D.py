import numpy as np
N = int(input())
AB = list(list(map(int, input().split())) for _ in range(N))
A, B = [np.array(i) for i in zip(*AB)]

AA = A * 2
C =  AA + B

C = np.sort(C)[::-1]

Taka = 0
Ao = np.sum(A)

for i in range(N):
	Taka += C[i]
	if Taka > Ao:
		break

print(i+1)