def consecutive(array1, array2):
    answer = 0
    i = 0
    j = 0
    while j < len(array2):

        if j < len(array2) and array1[i] == array2[j]:
            j += 1
            i += 1
        else:
            j = 0
            i += 1
        if j == len(array2):
            answer = 1
            break
        if i > len(array1):
            break
    return answer

n , m = input().split()
array1 = list(input().split())
array2 = list(input().split())

if consecutive(array1, array2)==1:
    print("Yes")
else:
    print("No")