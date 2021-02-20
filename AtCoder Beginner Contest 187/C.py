# N = int(input())
# S = list(str(input()) for i in range(N))

# ans = 'satisfiable'

# for i in range(N):
#     s = S.pop(0)
#     if s[0] == '!' and (s[1:] in S):
#         ans = s[1:]
#         break
#     if s[0] != '!' and ('!'+s in S):
#         ans = s
#         break
    
# print(ans)

N = int(input())
S = set(str(input()) for i in range(N)) #set!!!!!!!!!!!!!!!!!

ans = 'satisfiable'

for s in S:
    if "!" + s in S:
        ans = s
        break
    
print(ans)

# https://qiita.com/kitadakyou/items/6f877edd263f097e78f4

# in listはめちゃくちゃ遅い→ in set!!!!!!!!!!