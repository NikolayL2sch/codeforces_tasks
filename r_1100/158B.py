n = int(input())
a = [int(i) for i in input().split()]

left_ones = a.count(1)
left_twos = a.count(2)
left_threes = a.count(3)

ans = left_twos // 2 + left_threes + a.count(4)

if left_twos % 2 == 0:
    left_twos = 0
else:
    left_twos = 1

if left_ones > left_threes:
    left_ones -= left_threes
else:
    left_ones = 0

if left_twos == 1:
    if left_ones != 0:
        ans += (left_ones - 2) // 4 + ((left_ones - 2) % 4 != 0) + 1
    else:
        ans += 1
else:
    ans += left_ones // 4 + (left_ones % 4 != 0)

print(ans)
