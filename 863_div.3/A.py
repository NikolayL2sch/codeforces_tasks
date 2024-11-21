for _ in range (int(input())):
    n, d = map(int, input().split())
    s = input()
    for i in range(n):
        if int(s[n - i - 1]) >= d:
            print(s[:n - i:] + str(d) + s[n - i::])
            break
    else:
        print(str(d) + s)