n = int(input())
arr = list(map(int, input().split()))

l = len(arr) / n # 한 집합의 원소 갯수

arr.sort()
sumarr = [0] * n
s = 0
l = -1

for i in range(n):
    sumarr[i] = arr[s] + arr[l]
    s += 1
    l -= 1

sumarr.sort()

print(sumarr[-1])