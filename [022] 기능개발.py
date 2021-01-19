# 210119 기능개발

def solution(progresses, speeds):
    day = []
    answer=[]
    for p, s in zip(progresses, speeds):
        if len(day) == 0 or day[-1][0] < -((p-100)//s) :
            day.append([-((p-100)//s),1])
        else:
            day[-1][1] += 1
    for d in day :
        answer.append(d[1])
    return answer

#testcode
print(solution([93, 30, 55],[1, 30, 5])) #[2,1]
print(solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1])) #[1,3,2]
