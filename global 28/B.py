for _ in range(int(input())):
    n, k = map(int, input().split())
    ans = [0] * n
    cur_min = 1
    cur_max = n
    left_pos = 0
    right_pos = n - 1
    while cur_min <= cur_max and left_pos <= right_pos:
        if right_pos - left_pos + 1 >= k:
            for i in range(k - 1):
                if cur_min > cur_max or left_pos > right_pos:
                    break
                ans[left_pos] = cur_max
                cur_max -= 1
                left_pos += 1
                if cur_min > cur_max or left_pos > right_pos:
                    break
                ans[right_pos] = cur_max
                cur_max -= 1
                right_pos -= 1
        if cur_min > cur_max or left_pos > right_pos:
            continue
        ans[left_pos] = cur_min
        cur_min += 1
        left_pos += 1
        if cur_min > cur_max or left_pos > right_pos:
            continue
        ans[right_pos] = cur_min
        cur_min += 1
        right_pos -= 1

    print(*ans)