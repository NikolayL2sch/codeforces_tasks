for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    a.sort()
    flag = False
    i = 0
    j = n - 1
    while a[i] * a[j] != n - 2:
        if a[i] * a[j] < n - 2:
            i += 1
        elif a[i] * a[j] > n - 2:
            j -= 1
    print(a[i], a[j])
