for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    d = dict()
    ans = 0
    for num in a:
        if str(num) not in d:
            d[str(num)] = 0
        d[str(num)] += 1
    for i in sorted(d.values(), reverse=True):
        if i > 1:
            if i % 2 == 0:
                ans += i
            else:
                ans += i - 1
    print(ans // 2)
