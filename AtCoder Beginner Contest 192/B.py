S = input()
odd = True
ans = 'Yes'
o = ''
e = ''
for s in S:
    if odd:
        o = o+s
        odd = False
    else:
        e = e+s
        odd = True

if not o.islower():
    ans = 'No'

if not e.isupper() and e != '':
    ans = 'No'

print(ans)