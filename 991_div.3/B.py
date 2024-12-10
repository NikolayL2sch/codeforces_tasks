for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    if sum(a) % n != 0:
        print("NO")
    else:
        target = sum(a) // n
        sum_even = 0
        even_ind = 0
        sum_odd = 0
        odd_ind = 0
        for i in range(n):
            if i % 2 == 0:
                sum_even += a[i]
                even_ind += 1
            else:
                sum_odd += a[i]
                odd_ind += 1
        if sum_odd / target != odd_ind or sum_even / target != even_ind:
            print("NO")
        else:
            print("YES")
