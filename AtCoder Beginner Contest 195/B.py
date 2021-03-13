A, B, W = map(int, input().split())

minN = -(-(W*1000) // B)
maxN = (W*1000) // A

if minN <= maxN:
    print(minN, maxN)
else:
    print('UNSATISFIABLE')