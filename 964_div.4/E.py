from math import log

a = [int(log(i, 3)) + 1 for i in range(1, 2 * 10 ** 5 + 1)]

p = [0]
for i in range(1, 2 * 10 ** 5 + 1):
    p.append(a[i - 1] + p[i - 1])

for _ in range(int(input())):
    l, r = map(int, input().split())
    print(p[r] - p[l - 1] + a[l - 1])

