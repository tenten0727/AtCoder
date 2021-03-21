# N, M = map(int, input().split())
# S = list(int('0b1'+str(input()), 0) for _ in range(N))

# def has_duplicates(seq):
#     return len(seq) != len(set(seq))

# ans = 0
# for i in range(2**M, 2**(M+1)):
# 	bi = list(list(bin(i^s)) for s in S)
# 	nbi = list(b.count('1') for b in bi)
# 	print(nbi)
# 	if not has_duplicates(nbi):
# 		ans += 1
	
# print(ans)

# 問題の読み間違え