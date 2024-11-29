def find_div(n):
    d = set()
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            d.add(i)
            d.add(n // i)
    return d

for _ in range(int(input())):
    x, m = map(int, input().split())
    divs_x = find_div(x)
    divs_y = find_div(y)
    ans = 0
    for z in divisors:
        y = x ^ z
        if 1 <= y <= m and y != x:
            ans += 1
    print(ans)
