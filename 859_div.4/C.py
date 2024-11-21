t = int(input())

for i in range(t):
    n = int(input())
    s = list(input())
    if len(s) == 1:
        print("YES")
    else:
        flag = True
        checked = []
        for ch in s:
            if ch in checked:
                continue
            checked.append(ch)
            ind = -1
            for i in range(n):
                if s[i] == ch: 
                    if ind == -1:
                        ind = i % 2
                    elif ind != i % 2:
                        print("NO")
                        flag = False
                        break
            if flag == False:
                break
        if flag:
            print("YES")
        flag = True
        