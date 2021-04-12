N = input()
ans = 'Yes'
for i in range(1, len(N)+1):
	if N[-1] == '0':
		N = N[:-1]
	else:
		break

for i in range(0, len(N)):
	if N[i] != N[-(i+1)]:
		ans = 'No'
		break

print(ans)
