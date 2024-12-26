for _ in range(int(input())):
    n, a, b, c = map(int, input().split())
    days = 3 * (n // (a + b + c))
    left = n % (a + b + c)
    i = 0
    while left > 0:
        if i == 0:
            left -= a
        elif i == 1:
            left -= b
        elif i == 2:
            left -= c
        i += 1

    print(days + i)
