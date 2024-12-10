for _ in range(int(input())):
    l, r = map(int, input().split())
    L, R = map(int, input().split())
    if (l >= L) and (r <= R) or (L >= l) and (R <= r):
        ans = min(r, R) - max(l, L) + 2
        if l == L:
            ans -= 1
        if r == R:
            ans -= 1
    else:
        ans = min(R, r) - max(L, l) + 2
    if ans <= 0:
        ans = 1
    print(ans)
