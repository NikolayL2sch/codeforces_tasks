for _ in range(int(input())):
    a = input()
    if len(a) > 2:
        if len(a) == 3:
            if a[0] == '1' and a[1] == '0' and int(a[2]) >= 2:
                print('YES')
            else:
                print('NO')
        else:
            if a[0] == '1' and a[1] == '0' and int(a[2]) >= 1:
                print('YES')
            else:
                print('NO')
    else:
        print('NO')
