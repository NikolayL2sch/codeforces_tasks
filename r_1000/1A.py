n, m, a = map(int, input().split())

if n % a == 0:
    t1 = n // a
else:
    t1 = n // a + 1

if m % a == 0:
    t2 = m // a
else:
    t2 = m // a + 1

print(t1 * t2)
