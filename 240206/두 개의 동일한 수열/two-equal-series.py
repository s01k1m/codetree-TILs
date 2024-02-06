n = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

arr1.sort()
arr2.sort()

answer = "No"
for i in range(n):
    
    if arr1[i] != arr2[i]:
        break
    
    if i == n-1:
        answer = "Yes"

print(answer)