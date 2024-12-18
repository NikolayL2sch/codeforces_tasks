for _ in range(int(input())):
    n, m, q = map(int, input().split())
    b = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]
    b.sort()

    for pos in a:
        left = 0
        right = m - 1
        mid = 0
        while left <= right:
            mid = (left + right) // 2
            if b[mid] == pos:
                break
            if b[mid] < pos:
                left = mid + 1
            else:
                right = mid - 1

        if mid == 0 and b[mid] > pos:
            print(- 1 + b[mid])
        elif mid == m - 1 and b[mid] < pos:
            print(n - b[mid])
        elif b[mid] > pos:
            print((b[mid] - b[mid - 1]) // 2)
        else:
            print((b[mid + 1] - b[mid]) // 2)