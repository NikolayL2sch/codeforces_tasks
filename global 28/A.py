for _ in range(int(input())):
    n = int(input())
    n_str = str(n)
    while int(n_str) >= 33:
        if "33" in n_str and int(n_str) != 33:
            n_str = n_str.replace("33", "", 1)
        elif n >= 33:
            n_str = str(int(n_str) - 33)
        else:
            print("NO")
            continue
    if int(n_str) == 0:
        print("YES")
    else:
        print("NO")