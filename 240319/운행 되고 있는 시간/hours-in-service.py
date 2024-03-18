# 3 4 5 6 7 -> 4시간
# 1 2 3 4 -> 3시간

n = int(input())
arr = [
    tuple(map(int,input().split()))
    for _ in range(n)
]

ans = 0
for i in range(n): 
    time = [ 0
    for _ in range(1001)
    ] # 근무 시간 기록 array 초기화

    for index in range(n):
        if index == i: # i번째 직원을 이제 제외
            continue
        else:
            start, end = arr[index]
            for t in range(start, end): # 근무 시간 구간 기록
                time[t] = 1

    temp_ans = sum(time) # ‘운행 되고 있는 시간’

    ans = max(ans, temp_ans)

print(ans)