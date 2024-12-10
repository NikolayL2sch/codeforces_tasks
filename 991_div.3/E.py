for _ in range(int(input())):
    a = input()
    b = input()
    c = input()

    dp = [[float('inf')] * (len(b) + 1) for _ in range(len(a) + 1)]
    dp[0][0] = 0

    for i in range(len(a) + 1):
        for j in range(len(b) + 1):
            if i > 0:
                dp[i][j] = min(dp[i][j], dp[i - 1][j] + (a[i - 1] != c[i + j - 1]))
            if j > 0:
                dp[i][j] = min(dp[i][j], dp[i][j - 1] + (b[j - 1] != c[i + j - 1]))

    print(dp[len(a)][len(b)])