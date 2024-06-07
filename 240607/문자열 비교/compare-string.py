n, m = map(int, input().split())
S = [
    input()
    for _ in range(n)
]
ans = 0
def isInS(t):
    global ans, S
    if t in S:
        ans += 1

for _ in range(m):
    isInS(input())

print(ans)