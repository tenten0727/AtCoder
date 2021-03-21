N = int(input())

nlen = len(str(N))

A = list(9*(10**n) for n in range(int(nlen/2)-1))

ans = sum(A)
for i in range(10**int(nlen/2-1), 10**(int(nlen/2))):
	if i == 0:
		continue
	ss = str(i)+str(i)
	if int(ss) <= N:
		ans += 1
	else:
		break

print(ans)