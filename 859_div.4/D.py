t = int(input())

for i in range(t):
    n, q = map(int, input().split())
    a = [int(i) for i in input().split()]
    for j in range(q):
        l, r, k = map(int, input().split())
        s = 0
        for v in range(n):
            if l <= v + 1 <= r:
                continue
            s += (a[v] % 2)
        s += (k * (abs(r - l) + 1)) % 2
        s %= 2
        if s == 1:
            print("YES")
        else:
            print("NO")