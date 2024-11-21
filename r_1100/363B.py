"""
n одинаковых по ширине досок
высота i-ой доски hi
выломать k подряд идущих досок в заборе
k посл, сумма минимальна
"""

"""
Идея решения: предподсчет суммы, далее поиск минимальной разницы сумм где разность индексов = k
O (n + k)
"""

from typing import List

def sum_precount(a: List, n: int) -> List:
    precounted_list = [0] * (n + 1)
    precounted_list[1] = a[0]

    for i in range(1, n + 1):
        precounted_list[i] = precounted_list[i - 1] + a[i - 1]

    return precounted_list

n, k = map(int, input().split())
h = [int(i) for i in input().split()]
precounted_h = sum_precount(h, n)
min_sum = precounted_h[k] - precounted_h[0]
ans = 1
for i in range(1, n - k + 1):
    cur_sum = precounted_h[i + k] - precounted_h[i]
    if cur_sum < min_sum:
        min_sum = cur_sum
        ans = i + 1

print(ans)