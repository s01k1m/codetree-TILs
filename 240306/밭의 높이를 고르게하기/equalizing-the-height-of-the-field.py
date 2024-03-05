import sys

N, H, T = map(int, input().split())
# N개의 밭, 연속하게 최소 T 번 이상, H높이, 
arr = list(map(int, input().split()))

min_cost = sys.maxsize

for i in range(N-T+1):
    cost = 0
    new_arr = arr[i: i+T]
    
    for x in new_arr:
        cost += abs(x-H)

    min_cost = min(cost, min_cost)

print(min_cost)