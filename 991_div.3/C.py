for _ in range(int(input())):
    n = [int(i) for i in input()]
    mod = sum(n) % 9
    threes = n.count(3)
    twos = n.count(2)
    if mod == 0:
        print("YES")
    else:
        if threes > 0 and twos > 0:
            flag = False
            for i in range(threes + 1):
                for j in range(twos + 1):
                    if (mod - i * 3 + 2 * j) % 9 == 0:
                        print("YES")
                        flag = True
                        break
                if flag:
                    break
            else:
                print("NO")
        elif threes == 0:
            for j in range(twos + 1):
                if (mod + 2 * j) % 9 == 0:
                    print("YES")
                    break
            else:
                print("NO")
        elif twos == 0:
            for j in range(threes + 1):
                if (mod - 3 * j) % 9 == 0:
                    print("YES")
                    break
            else:
                print("NO")