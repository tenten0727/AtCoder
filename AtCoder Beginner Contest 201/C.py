import itertools
from typing import Iterable

S = list(input())

l = list(str(i) for i, s in enumerate(S) if s == 'o' or s == '?')
o = list(str(i) for i, s in enumerate(S) if s == 'o')
ans = 0
for v in itertools.product(l, repeat=4):
    s = ''.join(v)
    if all(x in s for x in o):
        ans += 1

print(ans)