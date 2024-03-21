# 반값 쿠폰 1개를 사용해서 선물 가능한 학생의 최대 명수를 구하기
N, B = map(int, input().split())
arr = [
    int(input())
    for _ in range(N)
]

# 최대한 많은 학생들을 선물하기 위해서 작은 가격부터 정렬한다
arr.sort()

ans = 0
# 반값 쿠폰 적용 완전탐색 시작

for idx in range(N):
    # print(arr)
    arr[idx] = arr[idx] // 2 # 반값 쿠폰 적용 참고, 선물의 가격은 항상 짝수입니다
    temp_arr = arr[::] # 최대한 많은 학생들을 선물하기 위해서 작은 가격부터 정렬한다
    temp_arr.sort()
    temp_students = 0 # arr[idx]에 반값 쿠폰 적용했을 때 선물 가능한 학생 수
    temp_sum = 0 # 그 학생들한테 선물했을 때 총 비용 
    start = 0 # 첫번째 학생 인덱스
    while (B-temp_sum >= temp_arr[start]): # 총 선물 비용이 최대 비용보다 작고 남은 금액이 더할 학생 보다 크거나 작은 동안에는
            temp_students += 1 # index 번째 학생 선물한다
            temp_sum += temp_arr[start] # 총비용에 더한다
            start += 1 # 다음 학생으로 넘어갈 준비를 한다
    
    ans = max(ans, temp_students)

    arr[idx] *= 2 # 선물비용 쿠폰 적용했던 것 원상 복구

print(temp_students)