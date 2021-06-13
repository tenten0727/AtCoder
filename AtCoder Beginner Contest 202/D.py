import math

A, B, K = map(int, input().split())

def func():
    count = 0
    i = 0
    a = A
    b = B
    s = ''
    while True:
        i += 1
        
        if i == A:
            s = s + 'b'
            if i != 1:
                count += math.factorial(b+i-1) / math.factorial(i-1) / math.factorial(b) + 1
            b = b-1
            i = 0
        if count + (math.factorial(b+i-1) / math.factorial(i-1) / math.factorial(b) + 1) > K:
            sa = list('a' for _ in range(a - i))
            s = s + ''.join(sa) + 'b'
            if i != 1:
                count += math.factorial(b+i-2) / math.factorial(i-2) / math.factorial(b) + 1
            a = i
            b = b-1
            i = 0
            
        print(a, b, i, count)
        if b == 0:
            sa = list('a' for _ in range(a))
            print(s + ''.join(sa))
            break
        if a == 0:
            sb = list('b' for _ in range(b))
            print(s + ''.join(sb))
            break
        
func()