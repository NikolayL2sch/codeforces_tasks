n = int(input())

coins = [int(i) for i in input().split()]
coins.sort()

s = 0
i = 0
while s <= sum(coins):
    s += coins.pop()
    i += 1

print(i)
