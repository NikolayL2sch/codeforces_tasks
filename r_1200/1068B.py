"""
число b
перебирает все a от 1 до 10^18
для каждого выписывает НОК(a, b) / a
сколько различных чисел на доске?
"""

"""
Идея решения:
НОД (a, b) * НОК (a, b) = a * b
=> НОК (a, b) / a = a * b / (a * НОД (a, b)) = b / НОД (a, b)
кажется, задача сводится к нахождению кол-ва делителей b
"""

def find_number_of_dividers(n):
    count = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            count += 1
            if i != n // i:  # Учитываем делители пары (i, n // i)
                count += 1
    return count

print(find_number_of_dividers(int(input())))
