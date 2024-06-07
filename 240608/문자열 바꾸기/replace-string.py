char1 = list(input())
char2 = list(input())
ans = 0

c1 = sorted(char1)
c2 = sorted(char2)

def isMatched(p1, p2):
    global ans
    if p1 != p2:
        ans +=1


if c1 != c2:
    print(-1)

else:
    for i in range(1, len(char1)):
        isMatched(char1[i], char2[i])

    print(ans)