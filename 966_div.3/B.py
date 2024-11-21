for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    taken = [False] * n
    for i in range(n):
        if i == 0:
            taken[a[i] - 1] = True
        else:
            if a[i] - 1 == 0:
                if not taken[a[i]]:
                    print('NO')
                    break
                else:
                    taken[a[i] - 1] = True
            elif a[i] == n:
                if not taken[a[i] - 2]:
                    print('NO')
                    break
                else:
                    taken[a[i] - 1] = True
            else:
                if not taken[a[i] - 2] and not taken[a[i]]:
                    print('NO')
                    break
                else:
                    taken[a[i] - 1] = True
    else:
        print('YES')
