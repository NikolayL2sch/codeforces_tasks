from bisect import bisect_left, bisect_right


def find_closest_elements(arr, i, n, R, L, a_i):
    target_r = R - a_i
    target_l = L - a_i

    right_index = bisect_right(arr, target_r, i + 1, n) - 1
    if right_index < i + 1:
        return -1

    '''
    if arr[right_index] <= target_r:
        print('here')
        right_index += 1
    '''

    # print(f'right_index for {i}: {right_index}')

    left_index = bisect_left(arr, target_l, i + 1, n)
    if left_index >= n or arr[left_index] < target_l:
        return -1
    # print(f'left index for {i}: {left_index}')
    if left_index > right_index:
        return -1
    return right_index - left_index


for _ in range(int(input())):
    n, x, y = map(int, input().split())
    a = [int(i) for i in input().split()]
    total_sum = sum(a)
    L = total_sum - y
    R = total_sum - x
    a.sort()
    count = 0
    for i in range(n):
        result = find_closest_elements(a, i, n, R, L, a[i])
        if result != -1:
            count+= result + 1

    print(count)