for _ in range(int(input())):
    n, m, k = map(int, input().split())
    ans = []
    for i in range(n, k - 1, -1):
        print(i, end=' ')
    for i in range(m + 1, k):
        print(i, end=' ')
    for i in range(1, m + 1):
        print(i, end=' ')
    print()