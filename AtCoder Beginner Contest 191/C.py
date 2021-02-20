# H, W = map(int, input().split())
# S = list(list(input()) for _ in range(H))
# left = -1
# right = -1
# ans = 0

# for i in range(1, H - 1):
#     white = True
#     l = -1
#     r = -1
#     for j in range(1, W):
#         if S[i][j] == '#' and white:
#             l = j
#             white = False
        
#         if S[i][j] == '.' and not white:
#             r = j-1
#             white = True
    
#     if l == -1 and r == -1:
#         continue

#     if left != l:
#         ans += 2
#         left = l
#     if right != r:
#         ans += 2
#         right = r

# print(ans)

H, W = map(int, input().split())
S = list(list(input()) for _ in range(H))
S = list(list(1 if s == '#' else 0 for s in S[i]) for i in range(H))
ans = 0

for i in range(1, H):
    for j in range(1, W):
        face = S[i-1][j-1] + S[i][j-1] + S[i-1][j] + S[i][j]
        if face == 1 or face == 3:
            ans += 1

print(ans)