for _ in range(int(input())):
    s = input()
    t = input()
    cur_id = 0
    ans = ''
    for i in range(len(s)):
        if s[i] == '?':
            if cur_id != len(t):
                ans += t[cur_id]
                cur_id += 1
            else:
                ans += 'a'
        elif cur_id == len(t):
            ans += s[i]
            continue
        elif s[i] == t[cur_id]:
            ans += s[i]
            cur_id += 1
        else:
            ans += s[i]
    if cur_id == len(t):
        print('YES')
        print(ans)
    else:
        print('NO')
