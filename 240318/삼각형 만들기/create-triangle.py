# 삼각형 만들기

n = int(input())
arr = [
    tuple(map(int,input().split()))
    for _ in range(n)
]
ans = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n ):
            p1, p2, p3 = arr[i], arr[j], arr[k] # 삼각형 점 후보를 선택
            x1, y1 = p1
            x2, y2 = p2
            x3, y3 = p3
            if ((x1- x2) == 0 or (x1-x3) == 0 or (x2-x3) == 0) and ((y1- y2) == 0 or (y1-y3) == 0 or (y2-y3) == 0):
                temp = abs((x1*y2 + x2*y3 + x3*y1)- (x2*y1 + x3*y2 + x1*y3))
                ans = max(ans, temp)
print(ans)