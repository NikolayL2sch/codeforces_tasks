from collections import deque


def can_cross_river(n, k, m, river):
    # Initialize BFS
    queue = deque([(0, 0, 1)])  # (position, in_water_distance, is_on_surface)
    visited = {(0, 0, 0)}

    while queue:
        pos, water_distance, on_surface = queue.popleft()

        # If we reach the right bank
        if pos >= n + 1:
            return True

        # If on the surface, consider jumps
        if on_surface:
            for jump in range(1, m + 1):
                new_pos = pos + jump
                if new_pos <= n and river[new_pos - 1] != 'C':
                    if river[new_pos - 1] == 'L':
                        cur_on_surface = 1
                    else:
                        cur_on_surface = 0
                    if (new_pos, water_distance, cur_on_surface) not in visited:
                        visited.add((new_pos, water_distance, cur_on_surface))
                        queue.append((new_pos, water_distance, cur_on_surface))
                elif new_pos >= n + 1:
                    return True

        # If in water, consider swimming
        if not on_surface:
            new_pos = pos + 1
            new_water_distance = water_distance + 1
            if new_pos <= n and river[new_pos - 1] != 'C' and new_water_distance <= k:
                if (new_pos, new_water_distance, 0) not in visited:
                    if river[new_pos - 1] == 'L':
                        cur_on_surface = 1
                    else:
                        cur_on_surface = 0
                    visited.add((new_pos, new_water_distance, cur_on_surface))
                    queue.append((new_pos, new_water_distance, cur_on_surface))
            elif new_pos >= n + 1 and new_water_distance <= k:
                return True

    # If the queue is exhausted without reaching the end
    return False


for _ in range(int(input())):
    n, m, k = map(int, input().split())
    river = input()
    if can_cross_river(n, k, m, river):
        print('YES')
    else:
        print("NO")