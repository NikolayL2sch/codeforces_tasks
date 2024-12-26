for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    gap = a[-1]
    for i in range(n - 1):
        if a[i] > b[i + 1]:
            gap += a[i] - b[i + 1]

    print(gap)
