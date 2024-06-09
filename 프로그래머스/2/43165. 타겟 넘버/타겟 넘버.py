def solution(numbers, target):
    answer = 0
    bfs = [0]
    count = 0
    
    for num in numbers:
        temp = []
    
        for item in bfs:
            temp.append(item + num)
            temp.append(item - num)
            
        bfs = temp
        
    for item in bfs:
        if item == target:
            count += 1
    
    answer = count
    return answer   