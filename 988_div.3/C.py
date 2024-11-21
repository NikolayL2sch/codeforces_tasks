for _ in range(int(input())):
    n, m, L = map(int, input().split())
    restrictions = []
    perks = []
    for i in range(n):
        restrictions.append(list(map(int, input().split())))
    for i in range(m):
        perks.append(list(map(int, input().split())))

    current_pos = 1
    current_jump_power = 1
    collected_boosts = 0

    restriction_id = 0
    perk_id = 0

    available_perks = []

    impossible = False

    while current_pos < L:
        if restriction_id >= n:
            break
        current_pos = restrictions[restriction_id][0] - 1
        while perk_id < m and perks[perk_id][0] <= current_pos:
            available_perks.append(perks[perk_id])
            perk_id += 1
        available_perks = sorted(available_perks, key=lambda x: x[1])

        next_restr_len = restrictions[restriction_id][1] - restrictions[restriction_id][0] + 2

        while next_restr_len > current_jump_power:
            if len(available_perks) == 0:
                impossible = True
                break
            current_jump_power += available_perks[-1][1]
            available_perks.pop()
            collected_boosts += 1
        if impossible:
            collected_boosts = -1
            break
        restriction_id += 1
    print(collected_boosts)
