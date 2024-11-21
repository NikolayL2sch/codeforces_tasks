t = int(input())

for i in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]
    m = 0
    b = 0
    for pack in a:
        if pack % 2 == 0:
            m += pack
        else:
            b += pack
    if m > b:
        print("YES")
    else:
        print("NO")
