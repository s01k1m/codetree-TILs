arr = [
    list(map(int,input().split()))
    for _ in range(2)
]

rowavg1 = sum(arr[0]) / 4
rowavg2 = sum(arr[1]) / 4

colavg1 = (arr[0][0]+arr[1][0]) / 2
colavg2 = (arr[0][1]+arr[1][1]) / 2
colavg3 = (arr[0][2]+arr[1][2]) / 2
colavg4 = (arr[0][3]+arr[1][3]) / 2
allavg = (rowavg1 + rowavg2)/2

print(f"{rowavg1:.1f} {rowavg2:.1f}")
print(f"{colavg1:.1f} {colavg2:.1f} {colavg3:.1f} {colavg4:.1f}")
print(f"{allavg:.1f}")