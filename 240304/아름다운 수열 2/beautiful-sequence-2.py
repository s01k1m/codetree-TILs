N, M = map(int,input().split())
arr_a = list(map(int, input().split()))
arr_b = list(map(int, input().split()))

#수열 A에서 길이가 M인 연속 부분 수열들 
#아름다운 수열 
bea = arr_b[::]
bea.sort()

def permutations(arr):
    if len(arr) <= 1:
        yield arr
    else:
        for perm in permutations(arr[1:]):
            for i in range(len(perm) + 1):
                yield perm[:i] + arr[0:1] + perm[i:]


ans = 0
for i in range(0, N+1-M):
        #수열 A에서 길이가 M인 연속 부분 수열들 
    a = arr_a[i:i+M]
    a.sort()

    flag= True

    for j in range(3):
        if a[j] != bea[j]:
            flag = False
    if flag:
        ans +=1

print(ans)