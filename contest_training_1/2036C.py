for _ in range(int(input())):
    s = input()
    q = int(input())
    found_substr = []
    start = 0
    cnt = s.count('1100')
    for j in range(q):
        i, v = map(int, input().split())
        before = s[max(0, i - 4): min(len(s), i + 3)].count('1100')
        s = s[:i - 1] + str(v) + s[i:]
        after = s[max(0, i - 4): min(len(s), i + 3)].count('1100')
        cnt += after - before
        if cnt > 0:
            print('YES')
        else:
            print('NO')