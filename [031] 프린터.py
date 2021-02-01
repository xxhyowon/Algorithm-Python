# 210201 프린터
# 대기목록에 있는 문서의 중요도가 순서대로 담긴 배열 priorities, 인쇄를 요청한 문서가 현재 대기목록의 어떤 위치에 있는지를 알려주는 location, 내가 인쇄를 요청한 문서가 몇 번째로 인쇄되는지 return

def solution(priorities, location):
    answer = 0
    while(len(priorities) > 0) :
        if location == 0 :
            if priorities[0] < max(priorities) :
                priorities.append(priorities.pop(0))
                location = len(priorities) - 1
            else :
                return answer + 1
        else :
            if priorities[0] < max(priorities) :
                priorities.append(priorities.pop(0))
                location -= 1
            else :
                priorities.pop(0)
                location -= 1
                answer += 1
    return answer

print(solution([1,1,9,1,1,1], 0)) #5