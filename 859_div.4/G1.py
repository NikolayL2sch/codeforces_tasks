t = int(input())

for i in range(t):
    n = int(input())
    a = [1]
    c = [int(i) for i in input().split()]
    cur_sum = 1
    cur_index = 0
    flag = True
    while cur_index < n:
        if c[cur_index] == cur_sum:
            cur_index += 1
        elif c[cur_index] > cur_sum:
            j = cur_index + 1
            cur_sum *= 2
            while j < n and c[j] <= cur_sum:
                cur_sum += c[j]
                j += 1
            if j == cur_index + 1:
                flag = False
                print("NO")
                break
            a = a[:j] + [cur_sum] + a[j:]
        else:
            j = cur_index + 1
            while j < n and c[j] < cur_sum - c[cur_index]:
                j += 1
            if j == n:
                print("NO")
                flag = False
                break
            a = a[:cur_index] + a[cur_index+1:j] + a[j+1:]
            cur_sum -= c[cur_index]
        cur_index += 1
    if flag:
        print("YES")