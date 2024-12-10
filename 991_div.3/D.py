for _ in range(int(input())):
    s = list(input())
    ans = ""
    for i in range(len(s)):
        if s[i] == "0":
            continue

        new_char = int(s[i]) - 1
        j = i - 1
        it = 0
        while j >= 0 and new_char > int(s[j]):
            it += 1
            j -= 1
            new_char -= 1
        if it > 0:
            for k in range(i, j + 1, -1):
                s[k] = s[k - 1]
            s[j + 1] = str(new_char + 1)

    print("".join(s))