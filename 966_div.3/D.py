for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    precounted_sum = [0] * (n + 1)
    precounted_sum[0] = 0
    for j in range(1, n + 1):
        precounted_sum[j] += precounted_sum[j - 1] + a[j - 1]
    print(f'Precounted sum: {precounted_sum}')
    s = input()

    dp = [0] * n
    left_L_pos = -1
    for i in range(n):
        if s[i] == 'L':
            if left_L_pos == -1:
                left_L_pos = i
            dp[i] = dp[i - 1]
        if s[i] == 'R':
            # print('found R at', i)
            if left_L_pos != -1:
                sum_interval = precounted_sum[i + 1] - precounted_sum[left_L_pos]
                dp[i] = max(dp[i], dp[left_L_pos] + sum_interval)
                left_L_pos = -1
    print(*dp)
