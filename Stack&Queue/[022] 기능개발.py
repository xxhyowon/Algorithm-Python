# 210119 기능개발
# 뒤에 있는 기능이 앞에 있는 기능보다 먼저 개발될 때 뒤에 있는 기능은 앞에 있는 기능이 배포될 때 함께 배포
# 작업의 진도가 배포되어야 하는 순서대로 적힌 정수 배열 progresses, 각 작업의 개발 속도가 적힌 정수 배열 speeds,한 번 배포할 때 몇 개의 기능이 배포되는지를 return

def solution(progresses, speeds):
    temp_list = []
    for p, s in zip(progresses, speeds):
        if len(temp_list) == 0 or temp_list[-1][0] < -((p-100)//s): # 앞에 기능보다 늦게 개발되면
            temp_list.append([-((p-100)//s),1]) #[배포까지 걸리는 날짜, 그 날 배포되는 기능 수]
        else: # 앞에 기능보다 빨리or동시에 개발되면
            temp_list[-1][1] += 1 # 앞에 기능이 배포될 때 배포되는 기능 수 +1
    answer = [d[1] for d in temp_list]
    return answer

#testcode
print(solution([93, 30, 55],[1, 30, 5])) #[2,1]
print(solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1])) #[1,3,2]
