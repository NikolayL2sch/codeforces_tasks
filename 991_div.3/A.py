for _ in range(int(input())):
    n, m = map(int, input().split())
    s = 0
    ans = -2
    for i in range(n):
        s += len(input())
        if s > m and ans == -2:
            ans = i
    if ans == -2:
        print(n)
    else:
        print(ans)
