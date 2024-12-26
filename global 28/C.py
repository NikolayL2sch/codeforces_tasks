for _ in range(int(input())):
    s = input()
    if s.find("1") == -1:
        print(1, len(s), 1, len(s) - 1)
        continue
    s1_start = s.find("1")
    s1 = s[s1_start::]
    if s1.find("0") == -1:
        print(s1_start + 1, len(s), s1_start + 1, s1_start + 2)
        continue
    s2_start = s1.find("0")
    s2 = s[s2_start::]
    translation_table = str.maketrans("01", "10")
    inverted_s2 = s2.translate(translation_table)
    int_s2 = int(inverted_s2, 2)
    found_pos = s1.find(inverted_s2)
    while found_pos == -1:
        int_s2 += 1
        s2 = str(bin(int_s2))[2:]
        found_pos = s1.find(inverted_s2)
    print(s1_start + 1, len(s), s1_start + 1, found_pos - s2_start + s1_start)