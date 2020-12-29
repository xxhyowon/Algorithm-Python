# 201222
# 문자열 내 p와 y의 개수 https://programmers.co.kr/learn/courses/30/lessons/12916

def solution(s):
    s = s.lower() # 대,소문자 구별하지 않아서 하나로 통일
    count_p = 0 # p 개수
    count_y = 0 # y 개수
    for i in range(len(s)): # 문자열s의 모든 인덱스를 차례로 순회
        if s[i] == 'p' :
            count_p += 1
        elif s[i] == 'y' :
            count_y += 1
    # if count_p == count_y :
    #     return True
    # else : # else값을 안주면 null값을 return
    #     return False
    return count_p == count_y # 조건문이 성립할 경우 True, 성립하지 않으면 False 반환

def solution(s):
    s = s.lower()
    return s.count('p') == s.count('y') # 집계함수 count

# testcode
print(solution("pPoooyY"))
print(solution("Pyy"))