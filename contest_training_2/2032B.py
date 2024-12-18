for _ in range(int(input())):
    n, k = map(int, input().split())
    elements_left = k - 1
    elements_right = n - k
    if elements_left == 0 and elements_right == 0:
        print(1)
        print(k)
    elif elements_left == 0 or elements_right == 0:
        print(-1)
    elif elements_left % 2 == 1 and elements_right % 2 == 1:
        print(3)
        print(1, *[k], k + 1)
    else:
        subarrays_left = 2
        subarrays_right = 2
        condition_1 = False
        condition_2 = False
        while subarrays_left <= elements_left and subarrays_right <= elements_right:
            if elements_left % 2 == subarrays_left % 2:
                condition_1 = True
            else:
                subarrays_left += 1
            if elements_right % 2 == subarrays_right % 2:
                condition_2 = True
            else:
                subarrays_right += 1

            if condition_1 and condition_2 and subarrays_left == subarrays_right:
                break
        else:
            print(-1)

        print(subarrays_left * 2 + 1)
        for i in range(1, subarrays_left + 1):
            print(i, end=' ')
        print(*[k], end=' ')
        for i in range(k + 1, k + subarrays_right + 1):
            print(i, end=' ')