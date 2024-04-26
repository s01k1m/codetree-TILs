n = int(input())
global l
l = n

global answer
answer = 0

arr = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

arr.sort(key=lambda x: x[1])
newArr = [False] * l




def is_seperated(array):

    # 겹치는 지 검사하기 전에 선분의 초기화
    before_start = 0
    before_end = 0

    flag = True

    for i in range(len(array)):
        if array[i]: # 선분 포함시킬때 검사 시작
            if (before_end and before_start): # 맨 처음 선분이 아니라면
                # 지금 선분의 시작과 끝
                start = array[i][0]
                end = array[i][1]
                if (before_end >= end >= before_start ) or (before_start <= start <= before_end): # 이전 끝나는 위치랑 시작 위치 겹치거나
                    flag= False

        return flag

def find_max(newArr, cnt):
    global answer
    if cnt == l:
        if (is_seperated(newArr)):
            temp = sum(newArr)
            answer = max(answer, temp)
            return # 종료 


    newArr[cnt] = False
    find_max(newArr, cnt+1)
    newArr[cnt] = True
    find_max(newArr, cnt+1)




find_max(newArr, 0)


print(answer)