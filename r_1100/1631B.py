"""
список a int len n
операция: выбрать подмассив a четного размера 2k, начинающийся в позиции l (1 <= l <= l + 2k - 1 <= n)
для каждого i принад. [0, k - 1], a[l + i] = a[l + k + i]

Пример:
a=[2,1,3,4,5,3] и выборе l=1 и k=2, проделывая описанную операцию, получим a=[3,4,3,4,5,3].

минимальное количество операций, чтобы сделать все элементы массива равными друг другу.
"""

"""
суть задачи: происходит копирование второй половины на первую

идея: найти максимальное количество подряд идущих элементов
так как копирование справа налево -> искать надо начинать справа
а не придется ли нам скопировать везде крайний правый элемент?
придется
в общем случае, когда крайний правый встречается лишь раз имеем ceil(log2(len(a)))
 
"""

for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]

    moves = 0
    cur_id = n - 1
    copying_elem = a[-1]
    current_copying_elems_in_row = 0
    while cur_id >= 0:
        while a[cur_id] == copying_elem and cur_id >= 0:
            current_copying_elems_in_row += 1
            cur_id -= 1
        if cur_id < 0:
            break
        cur_id -= current_copying_elems_in_row
        current_copying_elems_in_row *= 2
        moves += 1

    print(moves)