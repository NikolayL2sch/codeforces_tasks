for _ in range(int(input())):
    x, y = map(int, input().split())
    if y < -1:
        print("NO")
    else:
        print("YES")
