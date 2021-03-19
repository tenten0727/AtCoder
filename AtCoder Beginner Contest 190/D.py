N = int(input())

while N % 2 == 0:
    N //= 2

ans = 0
for i in range(1, int(N**0.5)+1):
    if N % i == 0:
        ans += 2

if int(N**0.5)*int(N**0.5) == N:
    ans -= 1

print(ans*2)


#約数を求める
# def make_divisors(n):
#     lower_divisors , upper_divisors = [], []
#     i = 1
#     while i*i <= n:
#         if n % i == 0:
#             lower_divisors.append(i)
#             if i != n // i:
#                 upper_divisors.append(n//i)
#         i += 1
#     return lower_divisors + upper_divisors[::-1]
