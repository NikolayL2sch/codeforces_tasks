n = int(input())
x = [int(x) for x in input().split()]
q = int(input())
m = []
for i in range(q):
    m.append(int(input()))

x.sort()  # Сортируем цены

for money_for_the_day in m:
    left = 0
    right = n - 1
    while left <= right:
        middle = (left + right) // 2
        if x[middle] <= money_for_the_day:
            left = middle + 1  # Идем вправо
        else:
            right = middle - 1  # Идем влево

    # `right` указывает на последний магазин, где цена <= money_for_the_day
    print(right + 1)
