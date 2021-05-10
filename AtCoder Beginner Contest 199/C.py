N = int(input())
S = input()
Q = int(input())

tab = list(list(map(int, input().split())) for _ in range(Q))

ans = list(S)
for q in range(Q):
	if tab[q][0] == 1:
		tmp = ans[tab[q][1]-1]
		ans[tab[q][1]-1] = ans[tab[q][2]-1]
		ans[tab[q][2]-1] = tmp
	else:
		ans = ans[N:]+ans[:N]

print("".join(ans))