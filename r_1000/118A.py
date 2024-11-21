letters = ('a', 'y', 'o', 'e', 'i', 'u')

s = input()
s = s.lower()
ans = ''
for e in s:
    if e not in letters:
        ans += '.'
        ans += e

print(ans)
