from math import sqrt

for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    s = 0
    days = 0
    for i in range(n):
        s += a[i]
        if int(sqrt(s)) == sqrt(s) and int(sqrt(s)) % 2 == 1:
            days += 1
    print(days)
