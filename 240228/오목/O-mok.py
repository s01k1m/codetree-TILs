black, white = False, False
cnt = 0
row = 0
col = 0
di = [0, 1, 1, -1]
dj = [1, 1, 0, 1]


arr = [
    list(map(int,input().split()))
    for _ in range(19)
]

def in_range(x,y):
    return 0<=x<19 and 0<=y<19

for i in range(19):
    for j in range(19):
        if white or black:
            continue

        for v in range(4):
            if white or black:
                continue

            cnt = 1

            nx = i+di[v]
            ny = j+dj[v]

            while in_range(nx,ny) and arr[nx][ny] == arr[i][j] and  arr[i][j] != 0:
                cnt += 1
                if cnt == 3:

                    row = nx + 1
                    col = ny + 1

                i = nx
                j = ny

                nx = i+di[v]
                ny = j+dj[v]



                if cnt == 5 and arr[i][j] == 2:
                    white = True
                    break
                elif cnt == 5 and arr[i][j] == 1:
                    black = True
                    break



if black:
    print(1)
    print(row, col)
elif white:
    print(2)
    print(row, col)
elif black == False and white == False:
    print(0)