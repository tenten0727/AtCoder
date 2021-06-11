S = input()
n = len(S)

def dfs(i, f):
    if i == n - 1:
        if sum(list(map(int, f.split("+")))) == 7:
            print(f.replace('+-', '-')+"=7")
            exit()
    else:
        dfs(i+1, f+"+"+S[i+1])
        dfs(i+1, f+"+-"+S[i+1])
    
dfs(0, S[0])