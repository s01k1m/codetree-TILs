import sys

min_dis = sys.maxsize
n = int(input())
arr = list(map(int, input().split()))

for i in range(n):
    # 기준이 i 임
    sum_dis = 0
    for j in range(n):
        if i == j:
            continue

        sum_dis += abs(i- j) * arr[j]

    min_dis = min(min_dis, sum_dis)
print(min_dis)