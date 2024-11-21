for _ in range(int(input())):
    a, b, c = map(int, input().split())
    for i in range(5):
        if min(a, b, c) == a:
            a += 1
        elif min(a, b, c) == b:
            b += 1
        elif min(a, b, c) == c:
            c += 1
    print(a * b * c)