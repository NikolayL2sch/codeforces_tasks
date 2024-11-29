for _ in range(int(input())):
    s = input()
    if len(s) == 1:
        print(-1)
        continue

    for i in range(0, len(s) - 2, 2):
        if len(set(s[i:i + 2:])) == 1:
            print(s[i:i + 2:])
            break
    else:
        for i in range(0, len(s) - 3, 3):
            if len(set(s[i:i+3:])) == 3:
                print(s[i:i+3:])
                break
        else:
            print(-1)
