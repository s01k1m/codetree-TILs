N = int(input())

if N == 1:
    print(0)
else:
    arr =[0] * 101
    for _ in range(N):
        place, alphabet = input().split()
        place = int(place)

        arr[place] = alphabet
    ans = 0

    for i in range(101):
        for j in range(i+1, 101):
            if arr[i] and arr[j]:
                new_arr = arr[i:j+1]
                if new_arr.count("G") == new_arr.count("H"):
                    ans = max(ans, j-i)
    
    print(ans)