for _ in range(int(input())):
    s = input()
    n = len(s)
    max_xor = 0
    result = (1, 1, 1, 1)

    if s.find("1") == -1:
        print(1, len(s), 1, len(s) - 1)
        continue

    s1_start = s.find("1")
    s1 = s[s1_start::]

    if s1.find("0") == -1:
        print(s1_start + 1, len(s), s1_start + 1, s1_start + 1)
        continue

    int_s1 = int(s1, 2)
    len_s2 = n - s.find("0")

    for k in range(s1_start, n - len_s2 + 1):
        s2 = int(s[k:k + len_s2], 2)
        xor_value = int_s1 ^ s2
        if xor_value > max_xor:
            max_xor = xor_value
            result = (s1_start + 1, n, k + 1, k + len_s2)

    print(*result)
