N = int(input())
S = list(input() for _ in range(N))

# def f(yi, i):
# 	ans = 0

# 	if i < 0:
# 		return 1

# 	if yi == 1:
# 		if S[i] == 'AND':
# 			ans += f(1, i-1)
# 		else:
# 			ans += 2*f(1, i-1)
# 			ans += f(0, i-1)
# 	else:
# 		if S[i] == 'AND':
# 			ans += 2*f(0, i-1)
# 			ans += f(1, i-1)
# 		else:
# 			ans += f(0, i-1)

# 	return ans


# print(f(1, N-1))

ans = 0

def f(s):
	ans = 0

	if len(s) == 0:
		return 1
	if s.pop() == 'AND':
		ans = f(s)
	else:
		ans = 2**(len(s)+1) + f(s)

	return ans

print(f(S))
	