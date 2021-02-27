
K = int(input())
S = list(str(input()))
T = list(str(input()))

S = map(int, S[:4])
T = map(int, T[:4])

SS = [0]*10
TT = [0]*10
cnt = [K]*10

for i in S:
	SS[i] += 1

for i in T:
	TT[i] += 1


sp = 0
tp = 0

for i in range(1, 10):
	cnt[i] = cnt[i] - SS[i] - TT[i]
	sp += int((i) * (10 ** SS[i]))
	tp += int((i) * (10 ** TT[i]))

ans = 0 #勝てるときの枚数
for i in range(1, 10):
	if cnt[i] == 0:
		continue
	for j in range(1, 10):
		if i == j or cnt[j] == 0:
			continue
		if sp + i*10**(SS[i]+1) - i*10**SS[i] > tp + j*10**(TT[j]+1) - j*10**TT[j]:
			ans += cnt[i] * cnt[j]

for i in range(1, 10):
	if cnt[i] < 2:
		continue
	if sp + i*10**(SS[i]+1) - i*10**SS[i] > tp + i*10**(TT[i]+1) - i*10**TT[i]:
		ans += cnt[i] * (cnt[i]-1)

print(ans / (9*K - 8) / (9*K - 9))


