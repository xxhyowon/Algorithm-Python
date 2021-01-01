# 210101
# 정수 제곱근 판별 https://programmers.co.kr/learn/courses/30/lessons/12934

import math

def solution(n):
    float_sqrt = math.sqrt(n) # 제곱근(실수타입)
    int_sqrt = int(math.sqrt(n)) # 정수타입 제곱근
 
    if float_sqrt == int_sqrt: #제곱근이 정수형태이면
        answer = (int_sqrt+1)**2
    else :
        answer = -1
    return answer

# testcode
print(solution(121))
print(solution(3))