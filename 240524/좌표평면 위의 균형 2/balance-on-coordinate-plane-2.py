# x, y 
# max_x, max_y를 하고 이거의 곱만큼의 완전탐색을 진행
# 1사분면 2, 3, 4을 어떻게 파악하지?
# (a, b)
# 1사분면 quadrant a > x, b > y 
# 2사분면 a < x, b > y
# 3사분면 a < x, b < y
# 3사분면 a > x, b < y

def compare(a, b, c, d):
    l = [a, b, c, d]
    return max(l)

n = int(input())
points = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

points.sort(key=lambda x:x[0])

min_x = points[0][0]
max_x = points[-1][0]

points.sort(key=lambda x:x[1])

min_y = points[0][1]
max_y = points[-1][1]


init = 100
ans = 100

for i in range (0, max_x + 1, 2):
    for j in range(0, max_y + 1, 2):

        segment = [0] * 5

        for x, y in points:
            # k번째 점이 몇사분면인지 확인하고 해당 위치의 segment를 1 증가시킵니다.
            if x > i and y > j:
                segment[1] += 1
            elif x < i and y > j:
                segment[2] += 1
            elif x < i and y < j:
                segment[3] += 1
            else:
                segment[4] += 1

        # x = i, y = j로 나눴을때의 m을 구합니다.
        cur_m = max(segment)

        ans = min(ans, cur_m)


print(ans)