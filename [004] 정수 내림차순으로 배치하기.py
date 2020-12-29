# 201224
# 정수 내림차순으로 배치하기 https://programmers.co.kr/learn/courses/30/lessons/12933

def solution(n):
    s = ''
    sorted_n = sorted(str(n), reverse=True)
    for i in sorted_n :
        s += i
    answer = int(s)
    return answer

def solution(n):
    sorted_n = sorted(str(n), reverse=True)
    answer = int(''.join(sorted_n)) # 리스트 문자열들을 합쳐주는 함수 join, 특정문자.join(리스트) : 리스트 내 문자열들을 특정문자로 연결
    return answer

# testcode
print(solution(118372))