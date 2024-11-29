for _ in range(int(input())):
    n = int(input())
    print(1, end=' ')
    for i in range(1, n - 1):
        print(i + (i + 1), end=' ')
    print(n - 1 + n)
