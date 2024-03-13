# 직사각형의 넓이를 최소로하는 프로그램을 작성해보세요.

n = int(input())
arr = [
    tuple(map(int,input().split()))
    for _ in range(n)
]

ans = 40000 * 40000

for i in range(n):
    # 초기화 여기서 했어야 했다
    minx = 40000
    miny = 40000

    maxx = 1
    maxy = 1

    for index, (x, y) in enumerate(arr):
        #  i 번째 점을 제외한다
        if index == i:
            continue
        minx = min(minx, x)
        miny = min(miny, y)
        maxx = max(maxx, x)
        maxy = max(maxy, y)

    temp_ans = (maxx - minx) * (maxy - miny)
    ans = min(temp_ans, ans)
    

print(ans)