S = input()
n = len(S)

def dfs(i, f):
    if i == n - 1:
        return sum(list(map(int, f.split("+"))))
    
    return dfs(i+1, f + S[i+1]) + dfs(i+1, f + "+" + S[i+1])

print(dfs(0, S[0]))

#sumを変数で使っててエラー