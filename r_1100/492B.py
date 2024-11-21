n, l = map(int, input().split())
a = [int(i) for i in input().split()]

a.sort()

d = max(a[0] - 0, l - a[-1])

for i in range(n - 1):
    d = max(d, (a[i + 1] - a[i]) / 2)

print(d)
