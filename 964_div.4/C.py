for _ in range(int(input())):
    n, s, m = map(int, input().split())
    prev_end = 0
    ans = False
    for i in range(n):
        cur_start, cur_end = map(int, input().split())
        if cur_start - prev_end >= s:
            ans = True
        prev_end = cur_end
        if ans:
            continue
    if m - prev_end >= s:
        ans = True
    if ans:
        print('YES')
    else:
        print('NO')
