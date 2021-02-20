V, T, S, D = map(int, input().split())

if V*T <= D and V*S >= D:
    print('No')
else:
    print('Yes')