def find_equal_pairs(lst):
    last_index = {}
    pairs = []

    for i, value in enumerate(lst):
        if value in last_index:
            pairs.append((last_index[value], i))
        last_index[value] = i

    return pairs


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    equal_pairs = find_equal_pairs(a)
    m = int(input())
    for i in range(m):
        s = input()
        if len(s) != len(a):
            print('NO')
            continue
        else:
            for pair in equal_pairs:
                if s[pair[0]] != s[pair[1]]:
                    print('NO')
                    break
            else:
                equal_pairs_str = find_equal_pairs([char for char in s])
                for p in equal_pairs_str:
                    if a[p[0]] != a[p[1]]:
                        print('NO')
                        break
                else:
                    print('YES')
