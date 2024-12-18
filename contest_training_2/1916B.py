from math import gcd

def find_min_divider(n):
    i = 3
    if n % 2 == 0:
        return 2

    while i * i <= n:
        if n % i == 0:
            return i
        i += 2
    return n

for _ in range(int(input())):
    a, b = map(int, input().split())
    if b % a == 0:
        print(b * (b // a))
    else:
        print(find_min_divider(a) * b)