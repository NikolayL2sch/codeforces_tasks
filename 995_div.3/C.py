for _ in range(int(input())):
    n, m, k = map(int, input().split())
    a = [int(i) for i in input().split()]
    q = set(map(int, input().split()))
    if len(q) == n:
        ans = m * '1'
        print(ans)
        continue
    elif len(q) != n - 1:
        ans = m * '0'
        print(ans)
        continue

    for elem in a:
        if elem in q:
            print('0', end='')
        else:
            print('1', end='')
    print()
