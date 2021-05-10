import itertools

N, M = map(int, input().split())

ab = list(list(map(int, input().split())) for _ in range(M))

ans = 0
color = [None for i in range(N)]
count = len(set(ab[:][0]+ab[:][1]))

per =  list(itertools.permutations(range(3), 2))

def f(m):
	global ans
	print(m)
	if m == M:
		ans += 1
		return

	a, b = ab[m][0]-1, ab[m][0]-1 
	if color[a] == color[b] and color[a] != None:
		return

	if color[a] == None and color[b] == None:
		for p in per:
			color[a] = p[0]
			color[b] = p[1]
			f(m+1)
			color[a] = None
			color[b] = None
	elif color[a] != None:
		for i in range(3).remove(color[a]):
			color[b] = i
			f(m+1)
			color[b] = None
	elif color[b] != None:
		for i in range(3).remove(color[b]):
			color[a] = i
			f(m+1)
			color[a] = None	

	return

	

f(0)
print(ans+3**(N-count))