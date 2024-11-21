def find_equal_pairs(lst):
    index_dict = {}
    pairs = []

    for _, value in enumerate(lst):
        if value in index_dict:
            # Если значение уже встречалось, добавляем пары с текущим индексом
            for j in index_dict[value]:
                pairs.append((j, _))
            index_dict[value].append(_)
        else:
            # Если значение встречается впервые, добавляем его в словарь
            index_dict[value] = [_]

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
            # print('Unequal length')
            continue
        else:
            for pair in equal_pairs:
                if s[pair[0]] != s[pair[1]]:
                    # print('Unequal value in str at index', pair[0], 'and', pair[1])
                    print('NO')
                    break
            else:
                equal_pairs_str = find_equal_pairs([char for char in s])
                for p in equal_pairs_str:
                    if a[p[0]] != a[p[1]]:
                        print('NO')
                        # print('Unequal value in list at index', p[0], 'and', p[1])
                        break
                else:
                    print('YES')
