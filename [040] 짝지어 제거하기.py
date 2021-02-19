# 210219 https://programmers.co.kr/learn/courses/30/lessons/12973

def solution(s):
    if len(s) % 2 == 1 :
        return 0
    answer = []
    
    for i in s :
        if len(answer) == 0 :
            answer.append(i)
        elif i == answer[-1] :
            answer.pop()
        else : answer.append(i)
    
    return 1 if len(answer) == 0 else 0

#testcode
print(solution("baabaa")) #1
print(solution("cdcd")) #0