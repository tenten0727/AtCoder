X = str(input())
X = list(X)
Y = list()
for x in X:
	if x != '.':
		Y.append(x)
	else:
		break


print(''.join(Y))