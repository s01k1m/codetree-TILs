import copy

ans = False

N = int(input())
original = [
    tuple(map(int, input().split()))
    for _ in range(N)
]
original.sort()

def straing(number, array, cnt):
    global ans
    global N
    global original

    if (sum(array) == N):
        ans = True
        return
    
    if cnt == 3:

        return

    else:
        a = number[cnt]
        newArray=copy.deepcopy(array)

        for idx, item in enumerate(original):
            # print(f'x는 {a} == {item[0]}')
            if item[0] == a:
                newArray[idx] = True

        straing(number, newArray, cnt+1)

        newArray=copy.deepcopy(array)
        for idx, item  in enumerate(original):
            # print(f'y는 {a} == {item[0]}')
            if item[1] == a:
                newArray[idx] = True

        straing(number, newArray, cnt+1)
        


for i in range(0,11):
    for j in range(0,11):
        for k in range(0,11):
            # (1, x) (x, 0) (x, 4)

            number = [i,j,k]
            straing(number, [False] * N, 0)

if ans == True:
    print(1)
else:
    print(0)