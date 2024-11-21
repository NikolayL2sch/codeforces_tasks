word = ['m', 'e', 'o', 'w']

for _ in range(int(input())):
    n = int(input())
    s = input().lower()
    j = 0
    i = 0
    ans = True
    while i < n:
        if j > 3:
            print("NO")
            ans = False
            break
        if s[i] != word[j]:
            print("NO")
            ans = False
            break
        else:
            i += s.count(word[j])
            j += 1
    if ans:
        print("YES")