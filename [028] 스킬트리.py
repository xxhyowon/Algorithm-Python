# 210127 스킬트리
# 선행 스킬 순서 skill과 유저들이 만든 스킬트리1를 담은 배열 skill_trees가 매개변수로 주어질 때, 가능한 스킬트리 개수를 return

def solution(skill, skill_trees):
    answer = 0
    for sk in skill_trees :
        skill_list = list(skill)
        for s in sk :
            if s in skill :
                if s != skill_list.pop(0) :
                    break
        else:
            answer += 1
    return answer

print(solution("CBD",["BACDE", "CBADF", "AECB", "BDA"])) #2