# 210201 프린터
# 대기목록에 있는 문서의 중요도가 순서대로 담긴 배열 priorities, 인쇄를 요청한 문서가 현재 대기목록의 어떤 위치에 있는지를 알려주는 location, 내가 인쇄를 요청한 문서가 몇 번째로 인쇄되는지 return

def solution(priorities, location):
    answer = 0 # 인쇄 요청 문서가 인쇄되는 차례
    while(len(priorities) > 0) :
        if location > 0 : # 인쇄 요청한 문서가 첫번째 문서가 아닐 때
            if priorities[0] < max(priorities) : # 첫번째 문서 중요도가 제일 크지 않으면
                priorities.append(priorities.pop(0)) # 마지막으로 이동
                location -= 1 # 인쇄 요청한 문서 위치
            else : # 첫번째 문서 중요도가 제일 크면
                priorities.pop(0) # 첫번째 문서 인쇄
                location -= 1
                answer += 1

        else : # 인쇄 요청한 문서가 첫번째 문서가 될 때
            if priorities[0] < max(priorities) :  # 인쇄 요청 문서 중요도가 제일 크지 않으면
                priorities.append(priorities.pop(0))
                location = len(priorities) - 1 
            else : # 인쇄 요청 문서 중요도가 가장 클 때
                return answer + 1 # 인쇄
    return answer

def solution(priorities, location):
    queue =  [(idx,p) for idx,p in enumerate(priorities)]
    answer = 0
    while True:
        front = queue.pop(0)
        if any(front[1] < q[1] for q in queue): # 첫번째 문서 보다 중요도가 큰 문서가 있다면
            queue.append(front) # 첫번째 문서 마지막으로 이동
        else: # 첫번째 문서 중요도가 제일 크면
            answer += 1 # 인쇄
            if front[0] == location: # 첫번째 문서가 인쇄 요청 문서라면
                return answer

print(solution([1,1,9,1,1,1], 0)) #5
