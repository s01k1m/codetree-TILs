everyone, limit, first, shake_times = map(int, input().split())
shake_record = [
    tuple(map(int, input().split()))
    for _ in range(shake_times)
]

shake_record.sort(key = lambda x: x[0]) # 악수 시간에 따른 오름차순 정렬

arr = [0] * (everyone + 1) # 전염병을 기록할 인원수 길이의 array
remaining_number_of_infection = [0] * (everyone + 1) # 점염 가능 잔여 횟수 기록용 array

arr[first] = True # 감염 기록
remaining_number_of_infection[first] = limit


for (t, x, y) in shake_record:
    if remaining_number_of_infection[x] > 0:
        if arr[y] == False:
            # 횟수 차감
            remaining_number_of_infection[x] -= 1
            # 새로운 감염
            arr[y] = True
            remaining_number_of_infection[y] = limit

        elif arr[y] == True: # 감염자 끼리의 만남
            remaining_number_of_infection[x] -= 1 # 횟수만 차감
            remaining_number_of_infection[y] -= 1

    elif remaining_number_of_infection[y] > 0:
        if arr[x] == False:
            # 횟수 차감
            remaining_number_of_infection[y] -= 1
            # 새로운 감염
            arr[x] = True
            remaining_number_of_infection[x] = limit
        elif arr[x] == True: # 감염자 끼리의 만남
            remaining_number_of_infection[x] -= 1 # 횟수만 차감
            remaining_number_of_infection[y] -= 1

for i in range(1, everyone + 1):
    if arr[i]:
        print(1, end= "")
    else:
        print(0, end= "")