import copy


N = int(input())
arr = [
    tuple(map(int, input().split()))
    for _ in range(N)
]
arr.sort()

def straing(number, array, cnt):
    global ans

    newArr = copy.deepcopy(array)

    if (len(newArr)== 0):
        ans = True
        return
    
    if cnt == 3:
        return
    else:
        a = number[cnt]

        for idx, item in enumerate(newArr):
            if item[0] == a:
                newArr.pop(idx)
        
        straing(number, newArr, cnt+1)

        newArr = copy.deepcopy(arr)
        for idx, item  in enumerate(newArr):
            if item[1] == a:
                newArr.pop(idx)
        straing(number, newArr, cnt+1)


ans = False

for i in range(0,10):
    for j in range(0,10):
        for k in range(0,10):
            # (1, x) (x, 0) (x, 4)

            number = [i,j,k]
            straing(number, arr, 0)

if arr == True:
    print(1)
else:
    print(0)