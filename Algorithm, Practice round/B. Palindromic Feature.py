s = str(input())
is_pal = lambda s1: s1 == s1[::-1]
best_pal = s

for bias in [1, 2]:
    for i in range(0, len(s) - bias):
        s1 = s[i:i+bias + 1]
        if is_pal(s1) and (len(best_pal) > len(s1) or (len(best_pal) == len(s1) and best_pal > s1)):
            best_pal = s1

print(best_pal if best_pal != s or is_pal(s) else -1)
