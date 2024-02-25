import sys
n = int(input())
arr = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

min_road = sys.maxsize
for i in range(1, n-1):
    new = arr[0: i] + arr[i+1: n] # 인덱스 i를 없앤 새로운 배열
    road = 0

    for j in range(n-2):
        road += abs(new[j][0] - new[j+1][0]) + abs(new[j][1] - new[j+1][1])
    min_road = min(min_road, road)
print(min_road)