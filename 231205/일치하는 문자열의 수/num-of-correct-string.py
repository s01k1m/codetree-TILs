n, word = input().split()
cnt = 0

for _ in range(int(n)):
    target = input()
    if target == word:
        cnt += 1

print(cnt)