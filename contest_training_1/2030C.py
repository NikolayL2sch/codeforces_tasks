for _ in range(int(input())):
    n = int(input())
    s = input()
    if s[0] == '1' or s[-1] == '1':
        print("YES")
        continue
    for i in range(1, n):
        if s[i - 1] == '1' and s[i] == '1':
            print("YES")
            break
    else:
        print("NO")