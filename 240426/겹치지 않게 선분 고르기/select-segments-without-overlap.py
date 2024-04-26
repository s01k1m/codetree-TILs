n = int(input())
answer = 0

arr = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

arr.sort(key=lambda x: (x[1],x[0]))
newArr = [False] * n



def is_seperated():
    global n
    # 겹치는 지 검사하기 전에 선분의 초기화
    before_start = 0
    before_end = 0
    global arr
    global newArr

    flag = True

    for idx in range(n):
        if newArr[idx]: # 선분 포함시킬때 검사 시작
            start = arr[idx][0]
            end = arr[idx][1]
            if (before_end and before_start): # 맨 처음 선분이 아니라면
                # 지금 선분의 시작과 끝
                if (before_end >= end >= before_start ) or (before_start <= start <= before_end) or (start<= before_start): # 이전 끝나는 위치랑 시작 위치 겹치거나
                    flag = False
                    return flag

            before_start = start
            before_end = end

    return flag

def find_max(cnt):
    global n
    global answer

    if cnt == n:
        if (is_seperated()):
            temp = sum(newArr)
            answer = max(answer, temp)
            return # 종료
        return


    find_max(cnt+1)
    newArr[cnt] = True
    find_max(cnt+1)
    newArr[cnt] = False



find_max(0)


print(answer)