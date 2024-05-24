arr = [
    list(map(int, list(input())))
    for _ in range(3)
]
# 팀으로 이겼다는 뜻은 한 줄에 팀을 이루고 있는 2개의 숫자가 적어도 하나씩은 등장해야함
ans = 0 
def win(a, b, c):
    global ans
    if len(list(set([a, b, c]))) == 2:
        ans += 1

for i in range(0, 3):
    win(arr[i][0],arr[i][1],arr[i][2])
    win(arr[0][i], arr[1][i], arr[2][i])
win(arr[0][0], arr[1][1], arr[2][2])
win(arr[2][0], arr[1][1], arr[0][2])

print(ans)