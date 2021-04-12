from itertools import permutations

S1 = input()
S2 = input()
S3 = input()


if len(S1) > len(S3) or len(S2) > len(S3):
	print('UNSOLVABLE')
	exit()

S = list(set(S1 + S2 + S3))
d = {}

for i, s in enumerate(S):
	d[s] = i

if len(S) > 10:
	print('UNSOLVABLE')
	exit()


for v in permutations(range(10), len(S)):
	if v[d[S1[0]]] == 0 or v[d[S2[0]]] == 0 or v[d[S3[0]]] == 0:
		continue

	n1 = 0
	for s in S1:
		n1 *= 10
		n1 += v[d[s]]
	
	n2 = 0
	for s in S2:
		n2 *= 10
		n2 += v[d[s]]
	
	n3 = 0
	for s in S3:
		n3 *= 10
		n3 += v[d[s]]

	if n1 + n2 == n3:
		print(n1)
		print(n2)
		print(n3)
		exit()
	
print('UNSOLVABLE')