for _ in range(int(input())):
    n, k = map(int, input().split())
    a = [int(i) for i in input().split()]
    a = sorted(a)[:len(a) - 1:]
    ans = 0
    for i in a:
        if i != 1:
            ans += 2 * (i - 1) + 1
        else:
            ans += 1
    print(ans)