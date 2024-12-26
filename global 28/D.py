def minimize_ranks(m, n, a, b):
    # Сортируем рейтинги участников и сложности задач
    a_sorted = sorted(a)
    b_sorted = sorted(b)

    # Массив для хранения минимальной суммы рангов для каждого k
    result = []

    # Для каждого возможного количества задач в одном соревновании
    for k in range(1, m + 1):
        total_rank = 0

        # Разбиваем задачи на соревнования
        competitions = m // k

        # Для каждого соревнования
        for i in range(competitions):
            # Сортируем задачи по сложности
            competition_tasks = b_sorted[i * k: (i + 1) * k]
            # Считаем количество задач, которые Кевин может решить
            kevin_solved = sum(1 for task in competition_tasks if task <= a_sorted[0])

            # Считаем ранги для всех участников
            for participant_rating in a_sorted:
                participant_solved = sum(1 for task in competition_tasks if task <= participant_rating)

                # Если участник решает больше задач, чем Кевин
                if participant_solved > kevin_solved:
                    total_rank += 1

            # Кевин всегда занимает 1-е место среди себя
            total_rank += 1

        # Добавляем результат для этого k
        result.append(total_rank)

    return result

for _ in range(int(input())):
    n, m = map(int, input().split())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    print(*minimize_ranks(m, n, a, b))