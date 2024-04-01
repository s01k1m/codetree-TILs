a, b =input().split()
ans = 0
for x in range(int(a), int(b)+1):
    x = list(map(int, list(str(x))))
    if len(set(x)) == 2:
        ans += 1

print(ans)