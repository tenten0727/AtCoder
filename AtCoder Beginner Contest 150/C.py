import math

N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

def small_count(N, R):
	count = 0
	for i in range(N):
		small = 0
		k = R.pop(0)
		sort = sorted(R)
		for s in sort:
			if k > s:
				small += 1
			else:
				break
		count += small*math.factorial(N-i-1)
	
	return count

p_count = small_count(N, P)
q_count = small_count(N, Q)

print(abs(p_count - q_count))
