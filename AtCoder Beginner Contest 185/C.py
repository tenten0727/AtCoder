# from math import factorial as fac

# L = int(input())

# ans = int(fac(L-1) / (fac(L-12) * fac(11)))

# print(ans)

from scipy.special import comb

L = int(input())
ans = comb(L-1, 11, exact=True) #exactを入れることで大きい値でも正確に計算

print(ans)