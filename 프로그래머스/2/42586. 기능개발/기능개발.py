

def processing(progresses, speeds):
    for i in range(len(progresses)):
        progresses[i] += speeds[i]

def solution(progresses, speeds):
    answer = []
    out = 0
    while len(progresses) != 0:
        if progresses[0] >= 100:
            speeds.pop(0)
            progresses.pop(0)
            out +=1
        
        if (len(progresses) != 0 and progresses[0] < 100 and out > 0) or (len(progresses) == 0 and out > 0):
            answer.append(out)
            print(answer, out, progresses)            
            out = 0
            
        if  len(progresses) != 0 and progresses[0] < 100:
            processing(progresses, speeds)


        
        
        
        
        
    return answer