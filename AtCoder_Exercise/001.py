N, L = map(int, input().split())
K = int(input())
A = list(map(int, input().split()))

l, r = 0, L
score = L // 2

while l <= r:
	cut = 0
	ncut = 0
	last = -1

	for a in A:
		if a - cut >= score:
			ncut += 1
			cut = a
		if ncut == K:
			last = L - cut
			break

	if last >= score:
		l = score + 1
	else:
		r = score - 1
	score = (l + r) // 2
	# print(l, r)

print(score)


#https://qiita.com/drken/items/97e37dd6143e33a64c8c

# def isOK(score):
# 	cut = 0
# 	ncut = 0
# 	last = -1

# 	for a in A:
# 		if a - cut >= score:
# 			ncut += 1
# 			cut = a
# 		if ncut == K:
# 			last = L - cut
# 			break

# 	if last >= score:
# 		return True
# 	else:
# 		return False


# def binary_search():
#     left = -1
#     right = L + 1 #場外はないけど一応
    
#     while right - left > 1:
#         mid = (right + left) // 2
#         if isOK(mid) == False:
#             right = mid
#         else:
#             left = mid
#     return left

# def main():
#     print(binary_search())

# if __name__ == "__main__":
#     main()